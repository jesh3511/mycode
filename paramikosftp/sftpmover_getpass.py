#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def transfer_to_this_remote_dir():
    while true:
        path = input(f"Please enter a remote path for the files to transfer to.\n")
            if path.startswith("/") and if path.endswith("/")
                break
            else   
                print("invalid path")
    return path

    
 main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## copy our firstpasswd.py script to bender
    sftp.put("file_to_move.txt", "file_to_move.txt") # move file to target location home directory
    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()
