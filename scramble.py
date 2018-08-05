import random

def scramble(string):
    pt1 = ""
    for i in range(4):
        pt1 += string[i+3] + string[i+8]
    pt1 += string[7]
    
    pt2 = ""
    start = 23
    for j in range(9):
        pt2 += string[start-j]
        
    pt3 = string[:3] + string[12:15] + string[24:27]
    
    string_new = pt1 + pt2 + pt3

    l = len(string_new)
    for i in range(len(string_new)/2):
        n = string_new[i+random.randint(0,len(string_new)/3)]
        string_new = string_new.translate(None, n)
        for i in range(l-len(string_new)):
            string_new += n
    return string_new
    
scrambled_message = "m/2hts/ttp:/fcpoc.lruynire6"
        
print scramble(scrambled_message)