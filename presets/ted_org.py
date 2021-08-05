from bs4 import BeautifulSoup


def ted_org(file_path):
    # Loading the file and parsing it
    file = open(file_path, "r")
    html = file.read()
    file.close()
    parsed = BeautifulSoup(html, 'lxml')


    # Checking if it was processed already
