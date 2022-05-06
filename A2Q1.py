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

str='Python is a case sensitive language'
print(len(str))
rev=str[::-1]
print(rev)
c=str[10:35]
print(c)
obj=str.replace('a case sensitive language','object oriented')
print(obj)
idx=str.index('a')
print(idx)
spc=str.replace(' ','')
print(spc)