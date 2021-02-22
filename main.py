import urllib
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import urlparse
from os.path import splitext, basename
import os
import re
#import lxml
import pytube

listOfLinks = []
level = 1
# youtube = pytube.YouTube("https://embed.ted.com/talks/merve_emre_how_do_personality_tests_work")
# stream = youtube.streams.all()
# for i in stream:
#   print(i)

regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"


def make_directories():
    IsJSDirExists = os.path.exists(os.getcwd() + "/JS/")
    if not IsJSDirExists:
        os.mkdir(os.getcwd() + "/JS/")
    IsCSSDirExists = os.path.exists(os.getcwd() + "/CSS/")
    if not IsCSSDirExists:
        os.mkdir(os.getcwd() + "/CSS/")
    IsImagesDirExists = os.path.exists(os.getcwd() + "/Images/")
    if not IsImagesDirExists:
        os.mkdir(os.getcwd() + "/Images/")


def save_index_html_file(htmlStr):
    try:
        htmlIndexFile = open(os.getcwd() + "/index.html", 'wb')
        htmlIndexFile.write(htmlStr.encode())
        htmlIndexFile.close()
    except IOError:
        print("Index File Exists!")


# req = urllib.request.Request("https://download.ted.com/talks/MerveEmre_PersonalityTests_2020E-light.mp4?apikey=acme-roadrunner", method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
# r = urllib.request.urlopen(req)
# r.getheader('Content-Type')
# # print(r.getheader('Content-Type'))
# disassembled = urlparse("https://download.ted.com/talks/MerveEmre_PersonalityTests_2020E-light.mp4?apikey=acme-roadrunner")
# filename, file_ext = splitext(basename(disassembled.path))
# print(filename)
# print(file_ext)

make_directories()
source = requests.get("https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/").text
soup = BeautifulSoup(source, "lxml")
index = str(soup)
for htmlElement in soup.find_all():
    for line in htmlElement:
        urls = re.findall(regex, str(line))
        for url in urls:
            for w in url:
                print(w)
                try:
                    req = urllib.request.Request(w, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
                    r = urllib.request.urlopen(req)
                    r.getheader('Content-Type')
                    disassembled = urlparse(w)
                    filename, file_ext = splitext(basename(disassembled.path))
                    if "image" in r.getheader('Content-Type'):
                        urllib.request.urlretrieve(w, os.getcwd() + "/Images/" + filename + file_ext)
                        index = index.replace(w, "./Images/" + filename + file_ext, 1)
                    if "html" in r.getheader('Content-Type'):
                        listOfLinks.append((level, w))
                    if "javascript" in r.getheader('Content-Type'):
                        try:
                            f = open(os.getcwd() + "/JS/" + filename + file_ext)
                        except IOError:
                            urllib.request.urlretrieve(w, os.getcwd() + "/JS/" + filename + file_ext)
                        finally:
                            index = index.replace(w, "./JS/" + filename + file_ext, 1)
                            f.close()
                    if "css" in r.getheader('Content-Type'):
                        try:
                            f = open(os.getcwd() + "/CSS/" + filename + file_ext)
                        except IOError:
                            urllib.request.urlretrieve(w, os.getcwd() + "/CSS/" + filename + file_ext)
                        finally:
                            index = index.replace(w, "./CSS/" + filename + file_ext, 1)
                            f.close()

                except:
                    urlExceptions = w.split("\"")
                    for w in urlExceptions:
                        try:
                            req = urllib.request.Request(w, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
                            r = urllib.request.urlopen(req)
                            r.getheader('Content-Type')
                            disassembled = urlparse(w)
                            filename, file_ext = splitext(basename(disassembled.path))
                            if "image" in r.getheader('Content-Type'):
                                urllib.request.urlretrieve(w, os.getcwd() + "/Images/" + filename + file_ext)
                                index = index.replace(w, "./Images/" + filename + file_ext, 1)
                            if "html" in r.getheader('Content-Type'):
                                listOfLinks.append((level, w))
                            if "javascript" in r.getheader('Content-Type'):
                                try:
                                    f = open(os.getcwd() + "/JS/" + filename + file_ext)
                                except IOError:
                                    urllib.request.urlretrieve(w, os.getcwd() + "/JS/" + filename + file_ext)
                                finally:
                                    index = index.replace(w, "./JS/" + filename + file_ext, 1)
                                    f.close()
                            if "css" in r.getheader('Content-Type'):
                                try:
                                    f = open(os.getcwd() + "/CSS/" + filename + file_ext)
                                except IOError:
                                    urllib.request.urlretrieve(w, os.getcwd() + "/CSS/" + filename + file_ext)
                                finally:
                                    index = index.replace(w, "./CSS/" + filename + file_ext, 1)
                                    f.close()
                        except:
                            # print("An exception occurred")
                            print()

index = index.replace("https", "")
index = index.replace("http", "")
save_index_html_file(index)

