#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     06-05-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
n=a^b
count=0
while n:
 n=n&(n-1)
 count=count+1
 continue
print("Required number of bits to be flipped:",count)