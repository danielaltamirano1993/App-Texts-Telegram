from asyncio import events
from os import name
import re
from telethon import TelegramClient, events, hints
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.tl.functions.messages import SendMessageRequest
import os

api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'


acc = []
os.chdir('./')
list = os.listdir()
for accs in list:
    try:
        if accs.split('.')[1] == 'session':
            acc.append(accs.split('.')[0])
    except:
        continue


linkgr = open('data/linkgr.txt','r',encoding='utf-8').read().splitlines()
print(linkgr)
chat = open('data/chat.txt','r',encoding='utf-8').read()

timesms = 5
timeacc = 5
        
for accs in acc:
    try:
        client = TelegramClient(accs, api_id, api_hash)
        async def main():
            for link_gr in linkgr:
                await client(JoinChannelRequest(link_gr))
                await client(SendMessageRequest(link_gr,chat))
                time.sleep(timesms)
        with client:
            client.loop.run_until_complete(main())
        time.sleep(timeacc)
    except:
        pass