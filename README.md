# Offline Kahn Academy Javascript Environment

This is my attempt to make Kahn Academy's JavaScript coding environment available offline.  The idea is to make this simple for my 8-year-old to use. With PyInstaller, this compiles to an exe file that should be placed in a folder next to the .html and .js files, then double clicked on.  Assumes that VSCode is installed and is in the path.

To build, run the following:

```
pip install pyinstaller
python -m PyInstaller --onefile serve.py
```
(The first line can be omitted after the first time building.)
