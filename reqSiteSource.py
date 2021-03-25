import urllib.request
import re
from bs4 import BeautifulSoup

# Pulls URL
response = urllib.request.urlopen("https://www.ted.com/talks/julian_burschka_what_your_breath_could_reveal_about_your_health")
webcontent = response.read()
f = open('stg.html','wb')
soup = BeautifulSoup(webcontent, "lxml")

# Saves block holding all ".mp4" links
mp4Link = soup.findAll(text=re.compile('.mp4'))
mp4LinkBlock = str(mp4Link) # For parsing

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



f.write(webcontent)
f.close