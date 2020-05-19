import socket
import sys 
import os 
import threading 
import requests
from requests.exceptions import HTTPError
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup




a= '''
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
          ; . . . .  - .        ,'
         : . . . .       _     /
        . . . . .          `-.:
       . . . ./  - .          )
      .  . . |  _____..---.._/ ____ DOLPHINS V1 BY: MOHAMMED BANYAMER _
~---~~~~----~~~~             ~~


'''
print (a) 
print("")
print("")
print ("-" * 60)
print ("                MULTI-SCANS FOR WEB ")
print ("-" * 60)
print("")
print("")
site = input("Enter a remote host to scan: ")
threads = 10
target = site

def ip():
	while site:
		

		try:
			ip = socket.gethostbyname(site)
			print("-" * 60 )
			print("The target ip is :" + ip)
			print("-" * 60 )
			

			break


		except ValueError :
			print("the site should be as strings ")
		else:
			break
ip()
def check_ping():
    hostname = site
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
        print ("-" * 60)
        print(pingstatus)
        print ("-" * 60)
    else:
        pingstatus = "Network Error"

    return pingstatus
pingstatus = check_ping() 
print("")



