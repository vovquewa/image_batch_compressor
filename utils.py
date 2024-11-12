"""
Utils for project
"""

import os
import logging

from pathlib import Path

from PIL import Image
from tqdm import tqdm

from constants import IMAGE_PIX_SIZE, IMAGE_QUALITY, COMPRESSED_DIR_ENDING, IMAGE_FORMAT_LIST
from config import log_config


def compress_image(file_path: str, max_pixels: int = IMAGE_PIX_SIZE) -> Image.Image:
    """
    Compress an image file to a maximum number of pixels.

    :param file_path: Path to the image file
    :param max_pixels: Maximum number of pixels in the output image
    :return: Compressed Image object
    """
    with Image.open(file_path) as img:
        width, height = img.size
        total_pixels = width * height

        if total_pixels > max_pixels:
            scale = (max_pixels / total_pixels) ** 0.5
            new_width = int(width * scale)
            new_height = int(height * scale)
            return img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return img.copy()


def save_image(
    img: Image.Image,
    file_path: str,
    quality: int = IMAGE_QUALITY,
    preserve_date: bool = False,
) -> None:
    """
    Save an image to a file with optimized settings based on the file format.

    :param img: Image object
    :param file_path: Path to the output file
    :param quality: JPEG compression quality (1-100)
    :param preserve_date: Whether to preserve the original file's creation and modification dates
    """
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in (".jpg", ".jpeg"):
        img.save(file_path, "JPEG", optimize=True, quality=quality)
    elif file_extension == ".png":
        img.save(file_path, "PNG", optimize=True)
    else:
        img.save(file_path, optimize=True)

    if preserve_date:
        original_stat = os.stat(file_path)
        os.utime(file_path, (original_stat.st_atime, original_stat.st_mtime))


def check_and_create_compressed_directory(directory: Path) -> Path:
    """
    Check if a directory exists and create it if it doesn't.

    :param directory: Path to the directory
    """
    logging.info("Checking if compressed directory exists: %s", directory)
    compressed_dir = directory.with_name(directory.name + COMPRESSED_DIR_ENDING)
    if os.path.exists(compressed_dir):
        logging.info("Compressed directory already exists: %s", compressed_dir)
        return compressed_dir
    if not os.path.exists(compressed_dir):
        logging.info("Creating compressed directory: %s", compressed_dir)
        os.makedirs(compressed_dir)
        logging.info("Compressed directory created: %s", compressed_dir)
        return compressed_dir


def compress_directory(directory):
    """
    Get a list of files to compress in a directory.

    :param directory: Path to the directory
    :return: List of file paths
    """
    if os.path.exists(directory):
        logging.info("Directory exists: %s", directory)
        source_list = get_image_files(directory)
        compressed_dir = check_and_create_compressed_directory(directory)
        result_list = get_image_files(compressed_dir)
        images_to_compress = compare_lists(source_list, result_list)
        for image in tqdm(images_to_compress, desc="Compressing images"):
            img = compress_image(os.path.join(directory, image))
            image_path = os.path.join(compressed_dir, image)
            save_image(img, image_path)
            log_config.result_logger.info("Compressed image: %s", image_path)


def get_image_files(directory):
    """
    Get a list of image files in a directory.

    :param directory: Path to the directory
    :return: List of image file paths
    """
    logging.info("Getting list of files to compress in directory: %s", directory)
    files = os.listdir(directory)
    files = [file for file in files if file.endswith(IMAGE_FORMAT_LIST)]
    logging.info("List of files to compress: %s", files)
    return files


def compare_lists(source_list, result_list):
    """
    Compare two lists of files and return the difference.

    :param source_list: List of source files
    :param result_list: List of result files
    :return: List of files that need to be compressed
    """
    logging.info("Comparing lists of files to compress")
    logging.info("Source list: %s", source_list)
    logging.info("Result list: %s", result_list)
    files_to_compress = [file for file in source_list if file not in result_list]
    logging.info("Files to compress: %s", files_to_compress)
    return files_to_compress
