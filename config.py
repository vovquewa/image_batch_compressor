"""
Configure file of project
"""

from logging.handlers import RotatingFileHandler
import logging

from constants import (
    LOGS_DIR,
    LOG_FORMAT,
    LOG_DT_FORMAT,
    MAX_BYTES,
    BACKUP_COUNT,
    LOG_FILE_PATH,
    LOG_FILE_COMPRESSED_PATH
)


class LogConfig:
    """
    Class to hold the result logger configuration.
    """

    def __init__(self):
        self.result_logger = None


log_config = LogConfig()


def configure_logging():
    """
    Configure logging settings for the application.

    :param log_file: Path to the log file (optional)
    """
    logs_dir = LOGS_DIR
    logs_dir.mkdir(exist_ok=True)

    # Common logging settings
    common_settings = {
        "level": logging.INFO,
        "maxBytes": MAX_BYTES,
        "backupCount": BACKUP_COUNT,
        "format": LOG_FORMAT,
        "datefmt": LOG_DT_FORMAT,
    }

    # Create formatter once and reuse
    formatter = logging.Formatter(
        fmt=common_settings["format"], datefmt=common_settings["datefmt"]
    )

    # Get the root logger
    root_logger = logging.getLogger()  # Get root logger
    root_logger.setLevel(common_settings["level"])

    # Clear any existing handlers
    root_logger.handlers.clear()

    # Configure root logger (basic logging)
    root_handler = RotatingFileHandler(
        LOG_FILE_PATH,
        maxBytes=common_settings["maxBytes"],
        backupCount=common_settings["backupCount"],
    )
    root_handler.setFormatter(formatter)
    root_logger.addHandler(root_handler)

    # Add console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Configure special logger (compressed images logger)
    log_config.result_logger = logging.getLogger("compressed_images_logger")
    log_config.result_logger.setLevel(common_settings["level"])

    # Create handler for compressed images
    result_handler = RotatingFileHandler(
        LOG_FILE_COMPRESSED_PATH,
        maxBytes=common_settings["maxBytes"],
        backupCount=common_settings["backupCount"],
    )
    result_handler.setFormatter(formatter)
    log_config.result_logger.addHandler(result_handler)
    log_config.result_logger.propagate = True
