"""
image batch compressor
mass image convertor from folder
"""

import os
import logging


from tqdm import tqdm

from config import configure_logging
from constants import IMAGE_FILES_DIRECTORY, COMPRESSED_DIR_ENDING
from utils import compress_directory


def main(directory=IMAGE_FILES_DIRECTORY):
    """
    Main function to compress all directories in a given directory.

    :param directory: Path to the directory containing directories to compress
    """
    configure_logging()
    category_directories = [
        directory.joinpath(d)
        for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]
    for category_directory in tqdm(
        category_directories, desc="Compressing category directories"
    ):
        logging.info("Compressing category directory: %s", category_directory)
        image_directories = [
            category_directory.joinpath(d)
            for d in os.listdir(category_directory)
            if os.path.isdir(os.path.join(category_directory, d))
            and not d.endswith(COMPRESSED_DIR_ENDING)
        ]
        for image_directory in tqdm(image_directories, desc="Compressing directories"):
            logging.info("Compressing directory: %s", image_directory)
            compress_directory(image_directory)
            logging.info("Directory compressed: %s", image_directory)
        logging.info("Directory compressed: %s", category_directory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise e
