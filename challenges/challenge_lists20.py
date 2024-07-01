#!/usr/bin/env python3
wordbank=["indentation","spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

print("There are",len(tlgstudents), "people in the class. \n")
app=input("Would you like to add any student names? (y/n)\n")
if app=="y":
    name=input("Enter the name of the student: \n")
    tlgstudents.append(name)
    print(name, 'entered succcessfully. \n')
    disp=input("Would you like to see an ammended list of the student names? (y/n) \n")
    if disp=="y":
        print(*tlgstudents, sep='\n')
    else:
        print("==END==")
elif app=="n":
    num=int(input("Enter the number of names to view from the list (1-20) : \n"))
    print(tlgstudents[:num:])
else:
    print("Please enter either 'y' or 'n' without the quotes. /n")




#enter num slices
#display