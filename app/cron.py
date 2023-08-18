print("STARTING CRON JOB")

import os
import requests
from time import sleep


def get_tags():
    try:
        ping_app = requests.get("https://procxy.onrender.com")
        nanom = "https://api.github.com/repos/nanopool/nanominer/releases/latest"
        lolm = "https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest"
        gmnr = "https://api.github.com/repos/develsoftware/GMinerRelease/releases/latest"
        nanom = requests.get(nanom).json()["tag_name"]
        gmnr = requests.get(gmnr).json()["tag_name"]
        lolm = requests.get(lolm).json()["tag_name"]
        return [nanom, lolm, gmnr]
    except:
        return ['v3.8.4', '1.76a', '3.41']

init_tags = get_tags()

while True:
    tags = get_tags()
    print(f"[ LOG ] : Versions: {tags}")
    if tags != init_tags:
        os.system("python prepare_lin.py")
        os.system("python prepare_win.py")
    sleep(60*60)
    init_tags = get_tags()
