#!/usr/bin/env python3
count = 0
with open("dracula.txt", "r") as vamp:
    for line in vamp:
        if "vampire" in line.lower():
            count += 1
            print(line)
            print(count)