import re

def split(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    sentences = re.sub(r'\n', '', content)
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
    sentences = re.sub(r'!\s', '!\n', sentences)
    sentences = re.sub(r'\?\s', '?\n', sentences)
    print(sentences)


split('number 4.txt')