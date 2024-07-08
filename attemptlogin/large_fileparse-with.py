#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    
    for line in kfile:
       
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 

print("The number of failed log in attempts is", loginfail)
