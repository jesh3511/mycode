#!/usr/bin/env python3
#libs
import shutil
import os
#begin main
def main()
    #change to github dir
    os.chdir('/home/student/mycode/mycode/')
    #move raynor to ceph dir
    shutil.move('raynor.obj', 'ceph_storage/')
    #prompt for new file name
    xname = input('What is the new name for kerrigan.obj? ')
    #move kerrigan
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
#call main
if__name__=="__main__":
    main()