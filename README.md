# IMAGE BATCH COMPRESSOR

## Overview

Image Batch Compressor is a Python utility that allows you to efficiently compress multiple images in batch while maintaining good visual quality. It automatically resizes and optimizes images to reduce their file size while preserving acceptable image quality.

## Features

- Batch processing of multiple images
- Maintains aspect ratio during compression
- Uses high-quality Lanczos resampling for optimal results
- Supports common image formats (JPEG, PNG, etc.)
- Simple command-line interface

## Requirements

- Python 3.12.2
- load-dotenv==0.1.0
- pillow==11.0.0
- python-dotenv==1.0.1
- tqdm==4.67.0

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Install required dependencies:
   pip install -r requirements.txt

3. Setup .env
   use .env.example

## Usage

```bash
python main.py

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Vladimir Kozlov
