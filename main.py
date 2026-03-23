import requests
import colorama
from colorama import Fore, Back, Style, init
import os
import time

init(autoreset=True)


def sendToWebhook():
    i = 0
    while i < times:
        time.sleep(0.5)
        response = requests.post(webhook, json=data)
        if response.status_code == 204:
            pass
        else:
            print(f"something went wrong: {response.status_code}")
        i = i + 1
        if i >= times:
            i = 0
            print("task concluded")
            time.sleep(5)
            break

while True:
    os.system("cls")

    print(Fore.MAGENTA + """$$$$$$$$\ $$\   $$\  $$$$$$\  $$\      $$\       $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
\____$$  |$$ |  $$ |$$  __$$\ $$$\    $$$ |      \__$$  __|$$  __$$\ $$  __$$\ $$ |      
    $$  / $$ |  $$ |$$ /  \__|$$$$\  $$$$ |         $$ |   $$ /  $$ |$$ /  $$ |$$ |      
   $$  /  $$$$$$$$ |\$$$$$$\  $$\$$\$$ $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
  $$  /   $$  __$$ | \____$$\ $$ \$$$  $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
 $$  /    $$ |  $$ |$$\   $$ |$$ |\$  /$$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ | \_/ $$ |         $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
\________|\__|  \__| \______/ \__|     \__|         \__|    \______/  \______/ \________|
                                                                                         
                                                                                         
                                                                                         """)
    webhook = input("Enter your webhook: >: ")
    text = input("What message should the webhook send?: >: ")
    times = int(input("How many times should the bot send that message?: >: "))

    data = {
        "content": text
    }
    sendToWebhook()