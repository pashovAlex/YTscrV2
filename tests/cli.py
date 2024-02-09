from scraper import getInnerHTML, scrapeVids
from mp3down import forLoop as downloader

def main():
    # plUrl = input("Enter playlist link: \n")
    # playlist = scrapeVids(getInnerHTML(plUrl))
    downloader(scrapeVids(getInnerHTML(input("Enter playlist link: \n"))))
    
if __name__ == '__main__':
    main()