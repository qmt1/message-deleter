import requests
from coloriz import Color
import time
import os

red = Color.RED
yellow = Color.YELLOW
cyan = Color.CYAN
green = Color.GREEN




def mdeleter():
    os.system('cls')
    print(Color.gradient(Color.blue_to_magenta, rf"""
$$\      $$\                                                                   
$$$\    $$$ |                                                                  
$$$$\  $$$$ | $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\        
$$\$$\$$ $$ |$$  __$$\ $$  _____|$$  _____| \____$$\ $$  __$$\ $$  __$$\       
$$ \$$$  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\   $$$$$$$ |$$ /  $$ |$$$$$$$$ |      
$$ |\$  /$$ |$$   ____| \____$$\  \____$$\ $$  __$$ |$$ |  $$ |$$   ____|      
$$ | \_/ $$ |\$$$$$$$\ $$$$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\       
\__|     \__| \_______|\_______/ \_______/  \_______| \____$$ | \_______|      
                                                     $$\   $$ |                
                                                     \$$$$$$  |                
                                                      \______/                 

                    By .qmt

                                                     _______             __             __                         
                                                    |       \           |  \           |  \                        
                                                    | $$$$$$$\  ______  | $$  ______  _| $$_     ______    ______  
                                                    | $$  | $$ /      \ | $$ /      \|   $$ \   /      \  /      \ 
                                                    | $$  | $$|  $$$$$$\| $$|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\
                                                    | $$  | $$| $$    $$| $$| $$    $$ | $$ __ | $$    $$| $$   \$$
                                                    | $$__/ $$| $$$$$$$$| $$| $$$$$$$$ | $$|  \| $$$$$$$$| $$      
                                                    | $$    $$ \$$     \| $$ \$$     \  \$$  $$ \$$     \| $$      
                                                     \$$$$$$$   \$$$$$$$ \$$  \$$$$$$$   \$$$$   \$$$$$$$ \$$      

    """))
    token = input(red + 'Token : ')
    cid = input(cyan + 'Channel ID : ')
    headers = {'Authorization':token}
    url = f'https://discord.com/api/v9/channels/{cid}/messages'

    message = requests.get('https://discord.com/api/v9/channels/1289662655711416363/messages',headers=headers)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        messages = response.json()  

        for message in messages:
            messageid = message['id']  
            durl = f'{url}/{messageid}'  
            res = requests.delete(durl, headers=headers)
            print(green + f'Message Deleted : {res.status_code}')
            time.sleep(0.4)



    else:
        print(red + "Error : ", response.status_code, response.text)
mdeleter()