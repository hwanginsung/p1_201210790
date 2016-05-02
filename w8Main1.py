word=raw_input()
b=dict()

def charCount(word):
    for c in word:
        if c not in b:
            b[c]=1
        else:
            b[c]=b[c]+1
    print b


charCount(word)

def lab8():
    charCount(word)
    
def main():
    lab8()