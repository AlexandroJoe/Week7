import string

file = open('ebook.txt','r')
text = file.read().lower()
updateText = ""
for texts in text:
    if texts not in string.punctuation:
        updateText += texts

text = updateText



def countWords(myStr):    
    myDict = {}
    splitWords = myStr.split() 
    for word in splitWords:
        myDict[word] = myDict.get(word,0)+1
        
    return myDict

result = countWords(text)
listed = list(result)

def happax(a):
    textlist = []
    for i in result:
        x = result[i]
        if x == 1:
            print(f"This is the happax {i} {x}")
            textlist.append(i)
    return textlist

y = [happax(listed)]
print(y)
# hl = []
# for i in hl:
#     if hl[i] == 1:
#         hl.append(i)
#     for word in hl:
#         print(word)
