import urllib.request
import urllib
import requests
import re
from bs4 import BeautifulSoup

# import wget
# import os
# import datetime
# import time
# import sys
# import platform
# from dateutil.relativedelta import relativedelta
# from threading import Thread
#
# try:
#     import requests
# except ImportError:
#     os.system("pip install requests")
#
#
# def download_file(url, local_fname):
#     try:
#         r = requests.get(url, stream=True)
#         with open(local_fname, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024):
#                 if chunk:
#                     f.write(chunk)
#
#         size = os.stat(local_fname).st_size / 1024
#         if size > 1100:
#             return True
#         else:
#             return False
#     except:
#         return False
#
#
# def play_video(vid_name):
#     os_name = platform.system()
#     if "Linux" in os_name:
#         os.system("xdg-open %s" % vid_name)
#     elif "Windows" in os_name:
#         os.system(vid_name)
#     elif "Darwin" in os_name:
#         os.system("open %s" % vid_name)
#
#
# def count_down(future):
#     diff = relativedelta(datetime.datetime.now(), future)
#     days = abs(diff.days)
#     hours = abs(diff.hours)
#     mins = abs(diff.minutes)
#     secs = abs(diff.seconds)
#     return "\r%d days, %d hours, %d mins %d secs left.." % (days, hours, mins, secs)
#
#
# def main():
#     target = datetime.datetime(2018, 1, 1, 00, 00, 00)
#     downloaded = False
#     print("Brought to you by Monro Coury... Happy New Year!")
#     while True:
#         try:
#             df = target - datetime.datetime.now()
#
#             sys.stdout.write(count_down(target))
#             time.sleep(1)
#             sys.stdout.flush()
#
#             if df.total_seconds() <= 300 and not downloaded:
#                 th = Thread(target=download_file, args=(url, "python_2018.mp4",))
#                 th.start()
#                 downloaded = True
#
#             if df.total_seconds() <= 4 and downloaded:
#                 play_video("python_2018.mp4")
#                 break
#
#         except KeyboardInterrupt:
#             sys.stdout.write("\nCouldn't wait eh? ._.")
#             break
#
#
# main()

<iframe width='560' height='315' src='c:/Users/mrciu/OneDrive/Documents/CRISTIAN/Web-Scraper/MattLangione_2020S-480p.mp4' type='video/mp4' frameborder='0' allowfullscreen></iframe>mp4LinkBlock = str(mp4Link) # For parsing

# Parsing through doc
counter = mp4LinkBlock.count(".mp4")
mp4LinkBlock.find(".mp4")
print(mp4LinkBlock.rfind('"'))


mp4Links = [] # Tags will be every even index, links will be odd indexes

# Finds first link and appends
currBlock = mp4LinkBlock
currFirstMP4 = currBlock.find(".mp4") + 4
tempBlock = currBlock[:currFirstMP4]
currLastQuote = tempBlock.rfind('"') + 1
# Splices first link and appends
currLink = mp4LinkBlock[currLastQuote:currFirstMP4]
mp4Links.append(currLink)
# Splices current block to view previous quotes for recent tag storage


# Finds tag prior to first link and appends
tempBlock = tempBlock[:]

print(mp4Links)

urllib.request.urlretrieve(mp4Links[0], '/Users/qadeer/Downloads/newFile.mp4')

f.write(webcontent)
f.close