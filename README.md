# FL-plugin-picker-nfo-creator
FL plugin picker nfo creator

## Usage
1. Create a folder called png in the same directory as the python file.

2. Download and place your plugin pictures within the png folder.

3. Name each file the same as the plugin name (check plugin database for accuracy) this is case sensetive.

4. Run program by calling `python create.py`

5. Copy contents of png folder to plugin database folder.

6. Done

## Requirements
Pillow

To install run: `pip install Pillow`

## Optional
You can adjust the resulting maximum image size by editing the python file and chaning the variable `maxsize`

Its recomended that x is 200 or less and y is 500 or less.

You can change the folder path by editing the `path` variable in the python file. (ensure that you use forward slashes and not backshalshes)
