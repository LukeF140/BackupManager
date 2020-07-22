BACKUP MANAGER
Created by Luke Fairs

This program is designed to compleate all backups at once without the need for user intervention once started.
There is also a built in restore tool so that theses backup files can be restored how the user wants.
All these tools are accessed through the 

The BackupManager.py should be ran and then from thier all functions can be accessed through commands.

This program gets the directorys and locations from the file 'BackupLocs.txt'
This file should be organised into pairs like stated.
	The first line of the pair should be the directory to be backed up:
		eg. C:\Users\ExampleUser\Pictures
	The second line of the pair should be the location where the backup file should be placed:
    		eg. C:\Backups

The backup will be a .zip folder using the following name covention:
	nameoffolder_BACKUP--DD-MM-YYYY_HH-MM.zip

The program can also restore backups.
The program will ask for the location of the backup including the backup file, this means the directory\backup_BACKUP--DD-MM-YYYY_HH-MM.zip
The program will also ask for the location for the backup to be restored to, here the parent folder where the folder will reside is all that is needed.
For example:
	There is the backup folder named 'Photos_BACKUP--22-07-2020_15-34.zip' in the directory 'C:\Backups'.
	The program wants you to input 'C:\Backups\Photos_BACKUP--22-07-2020_15-34.zip'
	The place where this folder wants to be restored is 'C:\Users\ExampleUser'
	You would input to the program 'C:\Users\ExampleUser' and then the program would create the folder 'C:\Users\ExampleUser\Photos' from the backup

IT IS IMPORTANT TO NOTE IF 'BackupLocs.txt' IS DELEATED OR LOST THEN THE DIRECTORYS AND THE LOCATION FOR THE BACKUPS WILL HAVE TO BE RE-ENTERED


THIS PROGRAM IS STILL UNDER DEVELOPMENT, SO NEW FEATURES ARE STILL BEING ADDED
BUGS SHOULD BE REPORTED THROUGH GitHub