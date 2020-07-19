# IMPORTS
import BackupCreator
import BackupRestore


# VARIABLES
contin = True


# FUNCTIONS
def Help():
    print("COMMANDS")
    print("  Help: Gives you this page of commands")
    print("  Backup: Does a backup of all directorys in backup list")
    print("  Restore: Opens menu for restoration of backups")
    print("  Exit: Exits program")


# MAIN
while contin:
    whatDo = input("\nWhat do you want to occur (type 'help' for list of commands): ").upper()
    
    if whatDo == "HELP":
        Help()
    elif whatDo == "BACKUP" or whatDo == "BACK UP":
        BackupCreator.Main()
    elif whatDo == "RESTORE":
        BackupRestore.Main()
    elif whatDo == "EXIT":
        print("Thank You for using BACKUP MANAGER")
        contin = False
    else:
        print("That command is unknown, try typing 'help' to see a list of commands")
    
