#!/usr/bin/env python

# This is the main entry point of our web crawler.
# It goes over every file downloaded by suckIT and downloads the content that suckIT missed
# (usually videos or other multimedia content that hugely relies on JS)
# Authors: Mark Motliuk, Arneet Singh Kalra, Qadeer Assan, Cristian Ciungu and Moayad.

import os
import sys
import time
from pathlib import Path

from presets.ted_org import ted_org

presets = {
    "ted.org": ted_org
}


def start(path, preset_str, sleep_time):
    preset = None

    for el in presets:
        if el == preset_str:
            preset = presets[el]

    if preset is None:
        print("Preset " + preset_str + " was not found")
        return

    if not os.path.isdir(path):
        print("Specified path is not a valid directory")
        return

    result = list(Path(path).rglob("*.html"))
    try:
        for file in result:
            preset(str(file), sleep_time)
    except KeyboardInterrupt:
        print("ENDED")
    except:
        time.sleep(1)
        start(path, preset_str, sleep_time)


if len(sys.argv) != 4:
    print("Not enough arguments specified")
    exit(1)

start(sys.argv[1], sys.argv[2], float(sys.argv[3]))
