"""
---------- BACKUP CREATOR ----------
Please read the README.txt for full details on the program and how it takes input and output
"""

# IMPORTS
import zipfile
import os
from os.path import basename
import re
from datetime import datetime


# VARIABLES
backups = {}
now = datetime.now()


# FUNCTIONS
# Reads file to find BackUps
def BackupsToCompleate():
    backupToDo = {}
    try:
        # Get Backup File
        backupFile = open("BackupLocs.txt", "r")
        fileCont = backupFile.readlines()
        backupFile.close()
        backUpFileInfo = []
        # Remove \n
        for E in fileCont:
            E = re.sub('\\n', '', E)
            if E != ' ':
                backUpFileInfo.append(E)
        # Sorts out directorys into dictionary
        for i in range(0, len(backUpFileInfo)):
            if i%2 == 0:
                try:
                    backupToDo[backUpFileInfo[i]] = backUpFileInfo[i+1]
                except:
                    print("ERROR: NO DICTIONARY FOR BACKUP TO BE PLACED")
                    return {}
        return backupToDo
    except:
        print("NO BACKUPS TO COMPLEATE")
        return {}

# Creates A BackUp (dirToBack: Directory to be backed up; backUpDir: Directory for the backup to be placed)
def CreateBackUp(dirToBack, backUpDir):
    if os.path.exists(dirToBack):
        if os.path.exists(backUpDir):
            # Create Name of Backup Folder
            backUpDir = backUpDir + "\\" + basename(dirToBack) + "_BACKUP--" + now.strftime("%d-%m-%Y_%H-%M") +".zip"
            print("\nBACKING UP DIRECTORY:  '" + dirToBack + "',  TO DIRECTORY:  '" + backUpDir + "'")
            # Create a ZipFile object
            with zipfile.ZipFile(backUpDir, 'w') as zipObj:
               # Go through all files in a Directory
               for folderName, subfolders, filenames in os.walk(dirToBack):
                   for filename in filenames:
                       # Create compleate file path for file
                       filePath = os.path.join(folderName, filename)
                       print("BACKING UP:", filePath)
                       # Add file to zip file
                       zipObj.write(filePath, os.path.relpath(filePath, dirToBack), zipfile.ZIP_DEFLATED)
            print("BACK UP COMPLEATED OF:  '" + dirToBack + "',  TO DIRECTORY:  '" + backUpDir + "'\n")
        else:
            print("ERROR: DIRECTORY '" + backUpDir + "' WAS NOT FOUND")
    else:
        print("ERROR: DIRECTORY '" + dirToBack + "' WAS NOT FOUND")

# Called from the main mannager
def Main():
    backups = BackupsToCompleate()
    for k in backups:
        CreateBackUp(k, backups[k])
