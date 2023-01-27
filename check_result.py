import requests
from bs4 import BeautifulSoup
import os
import time

URL = "http://www.mumresults.in"
r = requests.get(URL)

while True:
    soup = BeautifulSoup(r.content, "html5lib")
    table = soup.find("table", {"class": "countertwo"})
    rows = table.find_all("tr")

    website_sr = len(rows) - 2

    with open("current_sr.txt", "r") as file:
        current_sr = int(file.readlines()[0])

    if current_sr != None:
        if website_sr > current_sr:
            with open("current_sr.txt", "w") as file:
                file.write(str(website_sr))
            os.system("termux-media-player play buzzer.mp3")    
            os.system(
                f"termux-notification -c 'New result added!' --action 'termux-open-url {URL}; termux-media-player stop'"
            )

    time.sleep(30)
