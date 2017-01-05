#! python3
# organizeFiles.py - Moves files of same type to a new folder with the filetype as the name
# Ex: moves all powerpoints to folder .PPT. Used to clean up unorganized folders
# Usage: organizeFiles.py <path_of_folder_to_clean_up>

import os, sys, shutil

fileTypes = []

def organize(fol):

    # Finds and adds each filetype to a list for making folders
    for file in os.listdir(fol):
        # Grabs the file type, checks to see if its in the list, then makes sure its not blank, ie a folder
        if os.path.splitext(os.path.abspath(file))[1] not in fileTypes and os.path.splitext(os.path.abspath(file))[1] != '':
            fileTypes.append(os.path.splitext(os.path.abspath(file))[1])

    print(fileTypes)  # Show what file types were found

    # Make folder(s) named by filetype
    for fileType in fileTypes:
        try:                            # Error mitigation when running on a folder that already has already been organized
            os.chdir(fol)               # Changes the dir so mkdir makes folder inside folder your sorting
            os.mkdir(fileType.upper())  # Makes folder for each type of file
            print('Making folder called %s' % (fileType.upper()))
        except:
            continue

    # Moves files into sorted folders
    for folder in os.listdir(fol):
        for file in os.listdir(fol):
            if os.path.splitext(file)[1].upper() == str(os.path.split(folder)[1]) and os.path.splitext(file)[1] != '':
                print('Moving %s to %s' % (file, folder))
                filePath = os.path.abspath(file)                                    # Gets path for file
                folderPath = os.path.abspath(folder)                                # Gets path for folder
                shutil.move(os.path.abspath(filePath), os.path.abspath(folderPath)) # Moves file into appropriate folder

input = sys.argv[1]     # Allows input of the folder to be organized's path
organize(input)         # Runs the program on folder inputted