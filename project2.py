# -*- coding: utf-8 -*-
"""
The program should ask the user for the number of people attending the cookout 
and the number of hot dogs each person will be given.

Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

The program should display the following details:

• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over

NAME: Agostina Carluccio
COP1047C
"""
hotDogsPerPack = 10;
bunsPerPack = 8;

numPeople = int(input("Enter the number of people attending: "))
numHotdogs = int(input("Enter the number of hotdogs each person will have: "))

totalHotdogs = numPeople * numHotdogs

numHotdogsNeeded = totalHotdogs // hotDogsPerPack
numBunsNeeded = totalHotdogs // bunsPerPack
hotdogsLeftOver = totalHotdogs % hotDogsPerPack
bunsLeftOver = totalHotdogs % bunsPerPack

print("The minimum number of hotdog packages you need is", numHotdogsNeeded)
print("The minimim number of hotdog buns you need is", numBunsNeeded)
print("There would be", hotdogsLeftOver, " hotdogs left over")
print("There would be", bunsLeftOver, " hotdog buns left over")