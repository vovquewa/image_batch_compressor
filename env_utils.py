"""
Environment file utilities
"""

import os
import sys

def check_env_file():
    """
    Check if the environment file exists.
    If .env file is not found, exit the program.
    """
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(env_file):
        print("Error: .env file not found. Please create a .env file.")
        sys.exit(1)