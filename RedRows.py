# RedRows Verification
from urllib.request import urlopen

ct = 0

# BEFORE YOU RUN THE SCRIPT
# Alter the file path to match the location of the files on your device.
myfile = open("/Downloads/RedRows.css", "r")

for eachline in myfile.readlines():
    values = eachline.split()
    if(values[0] == "background-color:" and values[1] == "red;" ):
        ct += 1

myfile.close()

if(ct == 3):
    print("Success! Now search for the flag.")
    request = urlopen("https://nhscybersecurity.weebly.com/redrows.html")
    html = request.read()
    print(html)
else:
    print("Nope. Try again.")