#!/usr/bin/env python3

#Author: Mohamed Shaef
#Author: mshaef@myseneca.ca
#Date Created: 2024/09/23

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])

else:
    timer = 3
 
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
