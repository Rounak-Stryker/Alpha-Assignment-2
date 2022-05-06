#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     05-05-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-----------------------------------------------------------------------------

User_Input=str(input("Enter string: "))
index=User_Input.find('name')
if(index==-1):
    print("No")
else:
    print("Yes")