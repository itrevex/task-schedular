import os
from pathlib import Path


def get_file_path(file_name):
    return f"{Path(os.path.dirname(__file__))}/{file_name}"
