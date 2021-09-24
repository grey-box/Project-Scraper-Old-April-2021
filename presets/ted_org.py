import json
import time

import multithread

from bs4 import BeautifulSoup

def ted_org(file_path, sleep_time):
    # If it's index.html, replace /talks/ with talks
    if 'ted.com/index.html' in file_path:
        file = open(file_path, "r")
        html = file.read()
        file.close()

        file = open(file_path, "w")
        html = html.replace("/talks/", "talks/")
        file.write(html)
        file.close()

        return

    if 'ted.com/talks/' not in file_path:
        return
    # https://download.ted.com/products/99853.mp4
    # Loading the file and parsing it
    file = open(file_path, "r")
    html = file.read()
    file.close()

    if 'GB WATCH' in html:
        print("Skipped, since already processed")
        return

    parsed = BeautifulSoup(html, 'lxml')
    script = parsed.find_all(attrs={"data-spec": "q"})

    if len(script) != 1:
        return
    data = str(script[0])
    data = data.replace('<script data-spec="q">q("talkPage.init",{"el":"[data-talk-page]","__INITIAL_DATA__":', '', 1)
    data = data.replace('})</script>', '', 1)

    data_decoded = json.loads(data)['talks'][0]['downloads']['videoDownloads']
    # data_decoded = json.loads(data)['talks'][0]['downloads']['nativeDownloads']
    if data_decoded is None:
        print('Video is impossible to download')
        return

    # print(data_decoded)
    # 0 - low quality (180)
    # 1 - medium quality (480)
    # 2 - high quality (1080)
    data_decoded = str(data_decoded[0]['url'])
    download_path = file_path.replace('index_no_slash.html', '') + data_decoded.split('/')[-1]
    # todo does not always work
    download_object = multithread.Downloader(data_decoded, download_path)
    download_object.start()

    html = html.replace("Sign in", "GB WATCH", 1)
    html = html.replace('data-ga-action="signin"',
                        'onclick="window.open(\'/plyr.html?file=' + download_path + '\', \'_blank\').focus();return false"',
                        1)

    file_w = open(file_path, 'w')
    file_w.write(html)
    file_w.close()

    print('DONE')
    print(file_path)

    time.sleep(sleep_time)

    # exit(1)
