import os
import shutil
import requests
from io import BytesIO
from zipfile import ZipFile

bin_path = "bin_files"

nanom = "https://api.github.com/repos/nanopool/nanominer/releases/latest"
nanom = requests.get(nanom).json()
nanom = [asset["browser_download_url"] for asset in nanom['assets'] if "windows" in asset["name"]][0]
nanom_folder = nanom.split('/')[-1][:-4]

lolm = "https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest"
lolm = requests.get(lolm).json()
lolm_folder = lolm["tag_name"]
lolm = [asset["browser_download_url"] for asset in lolm['assets'] if "Win64" in asset["name"]][0]

gmnr = "https://api.github.com/repos/develsoftware/GMinerRelease/releases/latest"
gmnr = requests.get(gmnr).json()
gmnr = [asset["browser_download_url"] for asset in gmnr['assets'] if "windows" in asset["name"]][0]

nanom_zip = BytesIO(requests.get(nanom).content)
lolm_zip = BytesIO(requests.get(lolm).content)
gmnr_zip = BytesIO(requests.get(gmnr).content)

with ZipFile(nanom_zip) as zip:
    zip.extract(f"{nanom_folder}/nanominer.exe", path=f"{bin_path}/")
    zip.extract(f"{nanom_folder}/service.dll", path=f"{bin_path}/")

with ZipFile(lolm_zip) as zip:
    zip.extract(f"{lolm_folder}/lolMiner.exe", path=f"{bin_path}/")

with ZipFile(gmnr_zip) as zip:
    zip.extract(f"miner.exe", path=f"{bin_path}/")


os.rename(f"{bin_path}/{nanom_folder}/nanominer.exe", f"{bin_path}/nanom.exe")
os.rename(f"{bin_path}/{lolm_folder}/lolMiner.exe", f"{bin_path}/lolm.exe")
os.rename(f"{bin_path}/miner.exe", f"{bin_path}/gmnr.exe")

shutil.rmtree(f"{bin_path}/{lolm_folder}")
shutil.rmtree(f"{bin_path}/{nanom_folder}")