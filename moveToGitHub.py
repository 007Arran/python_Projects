#! python3
# moveToGitHub - another shitty program by me! Move's files from the path specified to the other path. Useful for this
# fancy new GitHub thingy.  Should make commits a lot easier

# Usage:
# move <og_path> <new_path>
# shortcuts include:
# GitHubPy in place of <new_path> to move file(s) to the GitHub python_Projects folder
# solidMech in place of <new_path> to move file(s) to the GitHub solidMech folder
# 'py YOURFILE' in place of <og_path> to move file(s) from python36

import os, sys, shutil

def move(old, new):

    # Check for a keyword
    if new == 'GitHubPy':
        new = 'C:\\Users\Arran\Documents\GitHub\python_Projects'
    if new == 'solidMech':
        new = 'C:\\Users\Arran\Documents\GitHub\solidMech'
    if old[0] == 'py':
        old = 'C:\\Users\Arran\AppData\Local\Programs\Python\Python36' + '\\' + old[1]

    print('The old path is %s' % old)
    print('The new path is %s' % new)
    # Move files/folders
    print('Moving %s to %s' % (old, new))
    filePath = os.path.abspath(old)      # Gets path for file
    shutil.copy(os.path.abspath(filePath), os.path.abspath(new))  # Moves file into appropriate folder

if len(sys.argv) > 2:
    ogpath = sys.argv[1:3]
    newpath = sys.argv[3]
else:
    ogpath = sys.argv[1]
    newpath = sys.argv[2]

move(ogpath,newpath)