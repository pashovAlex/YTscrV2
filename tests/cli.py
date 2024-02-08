from scraper import getInnerHTML, scrapeVids
from mp3down import forLoop as downloader
import sys

def main():
    plUrl = sys.argv[1]
    downloader(scrapeVids(getInnerHTML(plUrl)))
    
if __name__ == '__main__':
    main()