__version__ = "1.1.0"

from pathlib import Path


def _clean_characters(file_location: str) -> str:
    file_location = file_location.strip(" &'\"")
    file_location = file_location.replace("\ ", " ")
    file_location = file_location.replace("''", "'")
    return file_location


def get_dropped_file() -> Path:
    file_location = input("\n Drop File: ")
    file_location = _clean_characters(file_location)
    return Path(file_location).resolve()
