# IMAGE BATCH COMPRESSOR

## Overview

Image Batch Compressor is a Python utility that allows you to efficiently compress multiple images in batch while maintaining good visual quality. It automatically resizes and optimizes images to reduce their file size while preserving acceptable image quality.

## Features

- Batch processing of multiple images
- Maintains aspect ratio during compression
- Uses high-quality Lanczos resampling for optimal results
- Supports common image formats: JPEG, PNG

## Requirements

- Python 3.12
- load-dotenv==0.1.0
- pillow==11.0.0
- python-dotenv==1.0.1
- tqdm==4.67.0

## Installation Windows

### Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"

### Install pip

1. Download get-pip.py:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

2. Run:

```bash
python get-pip.py
```

### Install Git Bash (Windows)

[Download](https://gitforwindows.org) Git for Windows

Run the installer

During installation:

Choose default components

Select "Use Git from Git Bash only"

Choose "Checkout as-is, commit Unix-style line endings"

### Project Installation (for Windows use git-bash)

1. Go to project root dir

```bash
cd <path_where_project_will_be_installed>
```

1. Clone project

```bash
git clone https://github.com/vovquewa/image_batch_compressor.git
```

1. Go to project dir

```bash
cd image_batch_compressor
```

2. Create virtual environment

```bash
python -m venv venv
```

2. Activate venv

```bash
source venv/Scripts/activate
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Setup .env
   Use .env.example

```
IMAGE_FILES_DIRECTORY=<path_to_dir>
LOGS_DIR=<path_to_log_dir>
```

### Project update

```bash
git pull
```

## Usage

### Linux

```bash
python main.py

```

### Windows

Execute run.bat

or

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Vladimir Kozlov
