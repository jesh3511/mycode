#!/usr/bin/env python3
#libraries
import shutil
import os
#main
def main():
    #change to working dir
    os.chdir("/home/student/mycode/mycode/")
    #backup sdn
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    #backup 5g dir
    shutil.copytree("5g_research/", "5g_research_backup/")
if __name__=="__main__":
    main()
#end