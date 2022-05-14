from yarl import URL
import os
from dotenv import load_dotenv
load_dotenv()
import discord_notify as dn 

URL = os.getenv("URL")
def discord(message):
    notifier = dn.Notifier(URL)
    notifier.send(message, print_message=False)