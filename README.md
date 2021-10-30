# CLI-Dropfile

A simple way to get a filepath/pathlib.Path object via drag and drop in python3 CLI scripts.

Gets file/directory via drag and drop and return a Path object.

Asks for file or directory via drag and drop, strips unneeded characters,
and uses pathlib.Path to return a Path object.

Returns:

* (pathlib.PosixPath object): A pathlib.PosixPath object that can be used to get file path, filname, extension, etc.  

Issues:  

* Macs don't like filenames that include the { ' } character.  

## Sample Usage:

```py
# Import the module
import dropfile

# Call it and assign your filepath (pathlib.Path object)
p = dropfile.get()

# use Path methods, etc on your object
print(p)  # 'C:\somefolder\testfile.pdf'
print(p.parent)  # 'C:\somefolder'
print(p.stem)  # 'testfile'
print(p.suffix)  # '.pdf'
```
