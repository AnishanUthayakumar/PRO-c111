import os
import shutil

from_dir = "C:/Users/kumar/Downloads"
to_dir = "C:/Users/kumar/OneDrive - Peel District School Board/Desktop/Downloaded_files/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for fileName in list_of_files:
    name, extension = os.path.splitext(fileName)
    print(name)
    print(extension)