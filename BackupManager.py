# IMPORTS
import BackupCreator
import BackupRestore
import re


# VARIABLES
contin = True


# FUNCTIONS
def BackupList():
    backupList = {}
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
                    backupList[backUpFileInfo[i]] = backUpFileInfo[i+1]
                except:
                    print("ERROR: NO DICTIONARY FOR BACKUP TO BE PLACED")
                    return {}
        return backupList
    except:
        print("NO BACKUPS TO EDIT")
        return {}

def Help():
    print("COMMANDS")
    print("  Help: Gives you this page of commands")
    print("  Backup: Does a backup of all directorys in backup list")
    print("  Restore: Opens menu for restoration of backups")
    print("  Add Backup: Opens menu for adding a directory to be backed up")
    print("  Remove Backup: Opens menu for removing a directory from being backed up")
    print("  Exit: Exits program")

def AddBackup():
    backupFile = open("BackupLocs.txt", "a")
    backupPath = input("Input the path to the file to be backed up: ")
    backupToLoc = input("Input the location for the back up to be stored: ")
    backupFile.write(backupPath + "\n")
    backupFile.write(backupToLoc + "\n")
    backupFile.close()

def RemoveBackup():
    backupList = BackupList()
    backupPaths = []
    if backupList != {}:
        for k in backupList:
            backupPaths.append(k)

        for i in range(0, len(backupPaths)):
            print(str(i+1) + ". " + backupPaths[i])

        remove = int(input("Which backup do you want to remove (enter the number): ")) - 1
        
        backupFile = open("BackupLocs.txt", "r")
        lines = backupFile.readlines()
        backupFile.close()
        
        del lines[remove * 2 + 1]
        del lines[remove * 2]

        backupFile = open("BackupLocs.txt", "w")
        for line in lines:
            backupFile.write(line)
        backupFile.close()
        
        print ("REMOVED: '" + backupPaths[remove] + "' BACKUP")
    else:
        print ("THERE ARE NO BACKUP SET UP TO REMOVE")

    
# MAIN
while contin:
    whatDo = input("\nWhat do you want to occur (type 'help' for list of commands): ").upper()
    
    if whatDo == "HELP":
        Help()
    elif whatDo == "BACKUP" or whatDo == "BACK UP":
        BackupCreator.Main()
    elif whatDo == "RESTORE":
        BackupRestore.Main()
    elif whatDo == "ADD BACKUP" or whatDo == "ADD BACK UP":
        AddBackup()
    elif whatDo == "REMOVE BACKUP" or whatDo == "REMOVE BACK UP":
        RemoveBackup()
    elif whatDo == "EXIT":
        print("Thank You for using BACKUP MANAGER")
        contin = False
    else:
        print("That command is unknown, try typing 'help' to see a list of commands")
    
