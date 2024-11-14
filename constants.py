"""
Constants of project
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

IMAGE_PIX_SIZE = 250000
IMAGE_QUALITY = 70
MAX_BYTES = 10**6
BACKUP_COUNT = 2
COMPRESSED_DIR_ENDING = "_compressed"
IMAGE_FORMAT_LIST = (".jpg", ".jpeg", ".png")
BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = Path(os.getenv("LOGS_DIR"))
LOG_FILE_NAME = "main.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)
LOG_FILE_COMPRESSED_NAME = "result.log"
LOG_FILE_COMPRESSED_PATH = os.path.join(LOGS_DIR, LOG_FILE_COMPRESSED_NAME)
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
LOG_DT_FORMAT = "%Y-%m-%d %H:%M:%S"
IMAGE_FILES_DIRECTORY = Path(os.getenv("IMAGE_FILES_DIRECTORY"))
