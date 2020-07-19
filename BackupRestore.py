"""
---------- BACKUP RESTORE ----------
Please read the README.txt for full details on the program and how it takes input and output
"""

# IMPORTS
import zipfile
import os

# FUNCTIONS
# Restores the Backup (backupLoc: location of the backup; restoreTo: location for the files to be restored to)
def Restore(backupLoc, restoreTo):
    print("RESTORING FILES")
    backupZip = zipfile.ZipFile(backupLoc)
    backupZip.extractall(restoreTo)
    backupZip.close()
    print("RESTORED BACKUP: '" + backupLoc + "'  TO: '" + restoreTo)

# Called through main manager
def Main():
    print ("")
    # Gets location of backup and the place to restore to
    backupLoc = input("Please Enter the Location of the backup (encluding the backupfile): ")
    restoreLoc = input("Please Enter the location to restore your files to: ")

    # Gets the original name of the backup folder for the restored folder
    backUpFileName = os.path.basename(backupLoc)
    nameOfOrigFolder = backUpFileName.rsplit("_BACKUP", 1)
    folderName = nameOfOrigFolder[0]

    # Calles 'Restore()' to restore folders
    Restore(backupLoc, restoreLoc + "\\" + folderName)
