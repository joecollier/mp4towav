import os
from Tkinter import *
from tkFileDialog import *
from pathlib2 import Path

def getFilesFromFolderByFiletype(folder_selected, filetype):
    files_from_folder = []

    for root, dirs, files in os.walk(folder_selected):
        for file in files:
            if file.endswith(filetype):
                input_file = os.path.join(root, file)
                output_file = Path(getOutputFileFromInputFile(input_file))

                if not output_file.is_file():
                    files_from_folder.append(input_file)
    return files_from_folder

def getOutputFileFromInputFile(input_file):
    return input_file.replace(".mp4", ".wav")

def convertMp4ToWav(input_file):
    output_file =  getOutputFileFromInputFile(input_file)
    command = "ffmpeg -i \"{}\" \"{}\"".format(input_file, output_file)

    os.system(command)

root = Tk()
root.withdraw()
folder_selected = askdirectory()
filetype = ".mp4"

files = getFilesFromFolderByFiletype(folder_selected, filetype)
print (files)

for file in files:
    convertMp4ToWav(file)
