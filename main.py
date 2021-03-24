# Import statements
import urllib.request
from urllib.parse import urlparse
# import youtubescraper

# Provide link of web page to be stored locally
link = "https://www.ted.com/talks/julian_burschka_what_your_breath_could_reveal_about_your_health"

# Check what type of link we are working with:
domain = urlparse(link).netloc
print(domain)

# Create a copy of the source code of the web page
response = urllib.request.urlopen(link)
source_code = response.read()
# Store it in a new file -> source.html
f = open('source.html', 'wb')
f.write(source_code)
f.close


#urllib.request.urlretrieve('https://en.wikipedia.org/wiki/5G', 'video.mp4')