# RedRows Verification
"""
with open("/Downloads/RedRows.css", "a") as myfile:
    for x in range(0, 50):
        myfile.write("There are " + str(x) + " cars\n")
"""

with open("/Downloads/RedRows.css", "r") as myfile:
    print(myfile.read())
    
response2 = urllib2.urlopen("http://127.0.0.1:8080/winning")
html = response2.read()
print(html)

