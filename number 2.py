import os

file = open("number 2.txt",'r')
foutput = open("numbered number 2.txt",'w')#opening our output txt
a = 0
for i in file: #store the strings
    a += 1
    foutput.write('{:2d} {}'.format(a,i)) #format of the output
foutput.close()