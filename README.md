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

### Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"

### Install pip (if not already installed)

#### Windows:

1. Download get-pip.py:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

2. Run:

```bash
python get-pip.py
```

### Install Git Bash (Windows)

Download Git for Windows from git-scm.com

Run the installer

During installation:

Choose default components

Select "Use Git from Git Bash only"

Choose "Checkout as-is, commit Unix-style line endings"

### Project Installation

1. Go to project dir

```bash
cd image_batch_compressor
```

1. Clone project (for Windows use git-bash)

```bash
git clone https://github.com/vovquewa/image_batch_compressor.git
```

2. Create virtual environment

```bash
python -m venv venv
```

2. Install required dependencies:
   pip install -r requirements.txt

3. Setup .env
   use .env.example

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
