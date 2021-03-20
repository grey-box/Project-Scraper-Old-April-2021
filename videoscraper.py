# Author: Cristian Ciungu 
# Date: March 20th, 2021 

# This program downloads the YouTube video specified in the url variable and stores it in the Web-Scraper folder. 
# Note: this is just starter code; further modifications are needed to make the video scraper fully functional.  

import urllib.request
import urllib.error
import urllib.parse
import pafy
import youtube_dl 

url = 'https://www.youtube.com/watch?v=ezq_oPDu9bw'
video = pafy.new(url)
bestRes = video.getbest()
bestRes.download()
