import re

file = open("number 3.txt","r")
strings = re.findall('\w+',file.read()) #make the file into strings
avg = sum([len(strings)for a in strings])/len(strings)
print(avg)


file.close()
