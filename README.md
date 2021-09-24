# Web Scraper

Developing a web scraper to download specific web pages such that they can be viewed offline by a large number of people.

# Why
We are using [SuckIT](https://github.com/Skallwar/suckit) for downloading big complicated websites as it is very fast. However, it cannot handle multimedia content that relies on JS. That's why this repo was created.

The python script goes over all downloaded files, and injects content that SuckIT was not able to download. Primarily, that is video and images.

Each website requires a unique script that will download needed content. Those scripts are called `presets`; you can find the list of available presets below.

Creating presets should be easy. Please look at `main.py` and `presets/ted_org.py` for an example.


# Installation
```bash
# for multithreaded downloading
pip3 install multithread
# for progress bar
pip3 install tdqm
```

# Usage

```bash
./main.py <full path to the downloaded content> <preset name> <sleep time between processing files (seconds, can use values like `0.5`)>
```

## Available presets
- ted.org - [Ted](https://www.ted.com)
- 