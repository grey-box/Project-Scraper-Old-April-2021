# This is the main entry point of our web crawler.
# The goal is to develop a crawler that can download any web page including its HTML, CSS, JS alongside
# all content (videos, images, etc.)
# Authors: Arneet Singh Kalra, Qadeer Assan, Cristian Ciungu and Moayad.

# Import statements
import urllib.request
from urllib.parse import urlparse
import youtubescraper as ys

# Provide link of web page to be stored locally
link = "https://www.youtube.com/watch?v=VvGFL8yb9dM"  # Example web page

# Check what type of link we are working with:
domain = urlparse(link).netloc
print(domain)

# Depending on domain of link, decide which parser to run:
# One big user case is youtube
if domain == 'www.youtube.com':
    scraper = ys.YoutubeScraper(link)

# All other use cases (at the moment)
else:
    # Create a copy of the source code of the web page
    response = urllib.request.urlopen(link)
    source_code = response.read()
    # Store it in a new file -> source.html
    f = open('source.html', 'wb')
    f.write(source_code)
    f.close

    # TODO: Run an instance of Singlefile/Webarchive to download the HTML,CSS,JS of the webpage

    # TODO: Run through the original source_code to see if the website contains any videos

    # TODO: If the website contains a video, download the video and then embed it into the singlefile html code
        # urllib.request.urlretrieve(link, 'video.mp4')
