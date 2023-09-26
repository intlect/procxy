import os
import tarfile
import requests
import shutil
from io import BytesIO

try:
    bin_path = "bin_files"
    shutil.rmtree(bin_path)
    os.mkdir(bin_path)
except:
    pass

nanom = "https://api.github.com/repos/nanopool/nanominer/releases/latest"
nanom = requests.get(nanom).json()
nanom = [asset["browser_download_url"] for asset in nanom['assets'] if "linux" in asset["name"]][0]

lolm = "https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest"
lolm = requests.get(lolm).json()
lolm_folder = lolm["tag_name"]
lolm = [asset["browser_download_url"] for asset in lolm['assets'] if "Lin64" in asset["name"]][0]

gmnr = "https://api.github.com/repos/develsoftware/GMinerRelease/releases/latest"
gmnr = requests.get(gmnr).json()
gmnr = [asset["browser_download_url"] for asset in gmnr['assets'] if "linux" in asset["name"]][0]

rigel = "https://api.github.com/repos/rigelminer/rigel/releases/latest"
rigel = requests.get(rigel).json()
rigel_folder = rigel["tag_name"]
rigel = [asset["browser_download_url"] for asset in rigel['assets'] if "linux" in asset["name"]][0]

nanom_gz = BytesIO(requests.get(nanom).content)
lolm_gz = BytesIO(requests.get(lolm).content)
gmnr_gz = BytesIO(requests.get(gmnr).content)
rigel_gz = BytesIO(requests.get(rigel).content)



with tarfile.open(fileobj=nanom_gz) as tar:
    tar.extract("nanominer", path=f"{bin_path}/")

with tarfile.open(fileobj=lolm_gz) as tar:
    tar.extract(f"{lolm_folder}/lolMiner", path=f"{bin_path}/")

with tarfile.open(fileobj=gmnr_gz) as tar:
    tar.extract(f"miner", path=f"{bin_path}/")

with tarfile.open(fileobj=rigel_gz) as tar:
    tar.extract(f"rigel-{rigel_folder}-linux/rigel", path=f"{bin_path}/")

os.rename(f"{bin_path}/nanominer", f"{bin_path}/nanom")
os.rename(f"{bin_path}/{lolm_folder}/lolMiner", f"{bin_path}/lolm")
os.rename(f"{bin_path}/miner", f"{bin_path}/gmnr")
os.rename(f"{bin_path}/rigel-{rigel_folder}-linux/rigel", f"{bin_path}/rigel")
shutil.rmtree(f"{bin_path}/{lolm_folder}")
shutil.rmtree(f"{bin_path}/rigel-{rigel_folder}-linux")
