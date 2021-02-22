# Author: Arneet Singh Kalra
# This is a simple web scraper for youtube videos.
# It uses pytube to download videos and data regarding a specific youtube, provided through the URL link.
# A directory is created with the video title under YouTubeVideos. It contains the video thumbnail, video,
# as well as an HTML file that allows the content to be seen in any browser.

# If there are any bugs found, please contact me!

import sys
import os
import requests
import shutil
import pathlib
import string

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print('Error importing pytube {}'.format(e))

# Examples of youtube downloading
url = "https://www.youtube.com/watch?v=jI-HeXhsUIg&t=3s"

urls = [
    'https://www.youtube.com/watch?v=3UILJyJTI-c',
    'https://www.youtube.com/watch?v=vNaEBbFbvcY',
    'https://www.youtube.com/watch?v=xx4562gesw0',
    'https://www.youtube.com/watch?v=rcv_tYcRgw4',
    'https://www.youtube.com/watch?v=v3hd3AI2CAA'
]


def scrape(link):
    yt = YouTube(link)
    vid_title = yt.title

    # Clean title of video string
    temp = vid_title.translate(str.maketrans('', '', string.punctuation)) #Get rid of punctuation
    clean_title = temp.replace(" ","") #Get rid of white spaces

    # Create a directory to store video and text data
    # Python __file__ var allows directory to work on servers too
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + "/YouTubeVideos/" + clean_title

    # Create directory storing scraped content
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Download the video to the directory if the file does not already exist there
    if not os.path.isfile(path + "/video.mp4"):
        yt.streams.first().download(output_path=path, filename="video")
    else:
        print("Video already downloaded!")

    # Save thumbnail to the directory if not already downloaded
    if not os.path.isfile(path + "/thumbnail.jpg"):
        thumbnail = requests.get(yt.thumbnail_url).content
        with open(os.path.join(path, 'thumbnail.jpg'), 'wb') as handler:
            handler.write(thumbnail)
    else:
        print("Thumbnail already downloaded!")

    # Save original pointer to print to terminal temporarily
    original_stdout = sys.stdout

    # Save video data to HTML file in directory if not already downloaded
    # Save thumbnail to the directory if not already downloaded
    if not os.path.isfile(path + "/page.html"):
        with open(os.path.join(path, 'page.html'), 'w') as f:
            # Print to file instead of terminal
            sys.stdout = f
            print(
                '<!doctype html>\n'
                '<html>\n'
                '   <head>\n'
                f'       <title>{yt.title}</title>\n'
                '   </head>\n'
                '   <body>\n'
                '       <video width="640" height="360" controls>\n'
                f'           <source src="{path}/video.mp4" type="video/mp4">\n'
                '       </video>\n'
                f'       <h1>{yt.title}</h1>\n'
                f'       <h3>Author: {yt.author}</h3>\n'
                f'       <h3>Publish Date: {yt.publish_date}</h3>\n'
                f'       <h3>Rating: {yt.rating}</h3>\n'
                f'       <h3>Views: {yt.views}</h3>\n'
                '       <h3>Description: </h3>\n'
                f'          <p>Author: {yt.description}</p>\n'
                f'       <img src="thumbnail.jpg" alt="{yt.title} thumbnail" width="320" height="180">\n'
                '   </body>\n'
                '</html>\n'
            )
            # Reset printing to terminal
            sys.stdout = original_stdout
    else:
        print("HTML already downloaded!")

    print("Done scraping page!")


# Main Running point of file
scrape(url)

for a_url in urls:
    scrape(a_url)
