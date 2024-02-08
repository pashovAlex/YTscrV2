from scraper import getInnerHTML, scrapeVids
from mp3down import main as downloader

def main():
    plUrl = input("Enter playlist link: \n")
    playlist = scrapeVids(getInnerHTML(plUrl))
    for vids in playlist:
        for atrs in vids:
            downloader(atrs[1], atrs[0])
    
if __name__ == '__main__':
    main()