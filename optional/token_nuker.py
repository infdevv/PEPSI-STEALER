import aiohttp
import threading
import json
import asyncio
import requests
import colorama
from colorama import *

null = None
false = False
true = True

discord_api_version = 9
discord_api_base_url = f"https://discord.com/api/{discord_api_version}"

token = ""
invite_code = ""

async def get_session_id(sid):
  get_guild_endpoint = f"{discord_api_base_url}/invites/{invite_code}"

async def join_guild():
    join_guild_endpoint = f"{discord_api_baseurl}/invites/{invite_code}"
    join_guild_headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "", "X-Super-Properties": ""}
    join_guild_payload = {"session_id": sid}
    join_res = requests.post(join_guild_endpoint, json=join_guild_payload, headers=join_guild_headers)
	 
    if join_res.status_code in (200, 204, 201):
	    print(f"{Fore.GREEN}[>] succesfully joined guild")
    if join_res.status_code == 429:
	    print(f"{Fore.RED}[>] ratelimit has occured")
    if join_res.status_code == 403:
	    print(f"{Fore.RED} locked token, you can no longer use discords api")
    else:
	    print(f"{Fore.RED}[>] error has occured, response code {join_res}")

async def scrape_ids(fid)

async def dm_all():
  dm_url = f"{discord_api_base_url}/channels/{fid}/messages"
  dm_payload = {"content": "your friend has been hacked by r00tsec! ", "flags": 0, "tts": false, "mobile_network_type": "wifi", "nonce": fid}
  dm_headers = {"Content-Type": "application/json", "AUthorization": token}
  res = requests.post()
  if res.status_code in (200, 201, 204):
    print(f"{Fore.GREEN}[>] sent message")
async def main():
  async with aiohttp.ClientSession() as session:
    await join_guild()
    await scrape_ids()
    await dm_all()

asyncio.run(main())
