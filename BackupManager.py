# IMPORTS
import BackupCreator
import BackupRestore
import re


# VARIABLES
contin = True


# FUNCTIONS
def BackupList():
    backupList = {}
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

        try:
            remove = int(input("Which backup do you want to remove (enter the number): ")) - 1
        except:
            print ("ERROR: Number must be an Integer")
            return
            
        if remove >= 0 and remove < len(backupPaths):
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
            print("ERROR: NUMBER ENTERED IS TOO LARGE OR SMALL")
    else:
        print ("THERE ARE NO BACKUP SET UP TO REMOVE")

def List():
    backupList = BackupList()
    backupPaths = []
    if backupList != {}:
        for k in backupList:
            backupPaths.append(k)

        print("PATHS TO BE BACKED UP")
        for i in range(0, len(backupPaths)):
            print(str(i+1) + ". " + backupPaths[i])
    else:
        print("NO BACKUP PATHS")

def SpecificBackup():
    backupList = BackupList()
    backupPaths = []
    if backupList != {}:
        for k in backupList:
            backupPaths.append(k)

        for i in range(0, len(backupPaths)):
            print(str(i+1) + ". " + backupPaths[i])

        try:
            backDir = int(input("Which directory do you want to backup (enter the number): ")) - 1
        except:
            print ("ERROR: Number must be an Integer")
            return
            
        if backDir >= 0 and backDir < len(backupPaths):
            backupFile = open("BackupLocs.txt", "r")
            lines = backupFile.readlines()
            backupFile.close()

            backupLocInfo = []
            # Remove \n
            E = re.sub('\\n', '', lines[backDir * 2])
            if E != ' ':
                backupLocInfo.append(E)
            E = re.sub('\\n', '', lines[backDir * 2 + 1])
            if E != ' ':
                backupLocInfo.append(E)
            
            BackupCreator.CreateBackUp(backupLocInfo[0], backupLocInfo[1])
        else:
            print("ERROR: NUMBER ENTERED IS TOO LARGE OR SMALL")
    else:
        print ("THERE ARE NO DIRECTORYS SET UP TO BACKUP")

    
# MAIN
while contin:
    whatDo = input("\nWhat do you want to occur (type 'help' for list of commands): ").upper()
    
    if whatDo == "HELP":
        Help()
    elif whatDo == "BACKUP" or whatDo == "BACK UP":
        BackupCreator.Main()
    elif whatDo == "SPECIFIC" or whatDo == "SPECIFIC BACKUP" or whatDo == "SPECIFIC BACK UP":
        SpecificBackup()
    elif whatDo == "RESTORE":
        BackupRestore.Main()
    elif whatDo == "LIST" or whatDo == "LIST BACKUP" or whatDo == "LIST BACK UP":
        List()
    elif whatDo == "ADD" or whatDo == "ADD BACKUP" or whatDo == "ADD BACK UP":
        AddBackup()
    elif whatDo == "REMOVE" or whatDo == "REMOVE BACKUP" or whatDo == "REMOVE BACK UP":
        RemoveBackup()
    elif whatDo == "EXIT":
        print("Thank You for using BACKUP MANAGER")
        contin = False
    else:
        print("That command is unknown, try typing 'help' to see a list of commands")
    
