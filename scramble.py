import random

def scramble(string):
    l = len(string)
    for i in range(len(string)/2):
        n = string[i+random.randint(0,5)]
        string = string.translate(None, n)
        for i in range(l-len(string)):
            string += n
    return string
        
print scramble("https://tinyurl.com/2fcpre6")