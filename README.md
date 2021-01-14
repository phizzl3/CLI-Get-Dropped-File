# cli-get-file

A simple way to get a filepath/pathlib.Path object via drag and drop in python3 CLI scripts.

 Gets file/directory via drag and drop and return a Path object.

 Asks for file or directory via drag and drop, strips unneeded characters,
 and uses pathlib.Path to return a Path object.

 Returns:

* (pathlib.PosixPath object): A pathlib.PosixPath object that can be 
    used to get file path, filname, extension, etc. 

Sample Usage:

* p = get_file_path()
  * p = full path
  * p.parent = parent folder
  * p.stem = filename excluding extension
  * p.suffix = file extension

```py
# import the function
from getfile import get_file_path

# call it and assign your filepath (pathlib.Path object)
my_file = get_file_path()

# use Path methods, etc on your object
print(my_file.stem)  # 'testfile'
```
