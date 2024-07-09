#!/usr/bin/env python3


bot=int(input("Enter the number of bottles of beer: \n"))
#if bot == 1:
        
if bot <= 99:
    while bot > 1:
        print(f"{bot} bottles of beer on the wall!")
        print(f"{bot} bottles of beer! You take one down, pass it around!")
        print(f"{bot} bottles of beer on the wall!\n")
        bot -= 1
    if bot == 1:
        print(f"{bot} bottle of beer on the wall!")
        print(f"{bot} bottle of beer! You take one down, pass it around!")
        print(f"Now you've got no bottles of beer on the wall!\n")
else:
    print("type a number less than 99")    
    
    


    

