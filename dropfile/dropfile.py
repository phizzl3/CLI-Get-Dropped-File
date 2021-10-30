# 10.29.2021

from pathlib import Path


def get():
    """
    Gets file/directory via drag and drop and return a Path object.

    Asks for file or directory via drag and drop, strips unneeded characters,
    and uses pathlib.Path to return a Path object.

    Returns:
    - (pathlib.PosixPath object): A pathlib.PosixPath object that can be 
    used to get file path, filname, extension, etc. 

    Sample Usage:
    - p = dropfile.get()
        - p = full path
        - p.parent = parent folder
        - p.stem = filename excluding extension
        - p.suffix = file extension
    """
    # Get input file/folder and strip characters
    file_drop = input("\n Drop File: ")

    # Clean left and right characters
    file_drop = file_drop.strip(" &'\"")

    # Clean Windows character issues inside string
    file_drop = file_drop.replace("\ ", " ")
    file_drop = file_drop.replace("''", "'")

    # Set Path object and return
    return Path(file_drop).resolve()
