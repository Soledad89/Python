#!/usr/bin/python
# Filename: backup_ver1.py
import os 
import time
# 1. The files and directories to be backed up are specified in a list.
source = ['./dirforbackup/*']
# Notice we had to use double quotes inside the string for names with spaces in it.
# 2. The backup must be stored in a main backup directory
target_dir = './backup/' 
# Remember to change this to what you will be using
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
# 5. We use the zip command to put the files in a zip archive
clean_command = "rm -f {0}".format(target_dir) + '*'
cp_command = "cp {0} {1}".format(' '.join(source), target_dir)
zip_command = "gzip -r {0}".format(target_dir) + '*'
command = clean_command + " && " + cp_command + " && " + zip_command
# Run the backup
print(command)
if os.system(command) == 0:
    print('Successful backup')
else:
    print('Backup FAILED')
