import requests
print("""
   _       _           _           ___ _           _
  /_\   __| |_ __ ___ (_)_ __     / __(_)_ __   __| | ___ _ __
 //_\\ / _` | '_ ` _ \| | '_ \   / _\ | | '_ \ / _` |/ _ \ '__|
/  _  \ (_| | | | | | | | | | | / /   | | | | | (_| |  __/ |
\_/ \_/\__,_|_| |_| |_|_|_| |_| \/    |_|_| |_|\__,_|\___|_|
\n""")
print("Script by Abdulaziz\n")
print("Github : https://github.com/AbdulazizSherzodjanov \n")
print("Telegram : https://t.me/PyCoder_off1cial")
f = open("admin_pages.txt").readlines()
url = input("[*] Enter .txt sitelist ( for example sitelist.txt ) : ")
site_list = open(url).readlines()
pages = f
for i in pages:
  for sites in site_list:
    url2 = (f"{sites}{i}")
    req = requests.post(url2)
    a = req.status_code
    if a == 404:
      print(f"\u001b[31mPage not found >> {a} >>> {url2}\u001b[31m")
    else:
      print(f"\u001b[32mPage found >> {url2}\u001b[32m")
      break