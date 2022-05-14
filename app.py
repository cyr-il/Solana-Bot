from dataclasses import is_dataclass
from ntpath import join
from typing import final
import requests
from bs4 import BeautifulSoup
import log

def split(word):
    return list(word)
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
URL = "https://coinmarketcap.com/fr/currencies/solana/"

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.encode("utf-8")

price = soup.find('div', class_='priceValue').get_text()
finalPrice = []
for caract in price:
    finalPrice.append(caract)
var = "".join(str(e) for e in finalPrice)
finalPrice.pop(0)
finalPrice.pop(2)
integers = [int(i) for i in finalPrice]
strings = [str(integer) for integer in integers]
a_string = "".join(strings)
an_integer = int(a_string)
solanaValue = float(an_integer / 100)
if (solanaValue > 48):
    log.discord("Achète du Solana car le prix est maintenant de {} €".format(solanaValue))