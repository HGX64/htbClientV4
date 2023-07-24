#!/usr/bin/python3 

import requests,json,getpass
url = "https://www.hackthebox.eu/api/v4/login"
email = input("Email: ")
password = getpass.getpass()

headers = {"User-Agent":"pyhtb" , "Accept":"application/json"}
data = {"email":f"{email}","password":f"{password}"}

try :
    r = requests.post(url,data=data,headers=headers)
    data = json.loads(r.text)
    print(data['message']['access_token'])
except:
    print("\n\n[!] Invalid login\n")
