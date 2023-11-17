from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

pl_url = "https://youtube.com/playlist?list=PLKq6LCtE6MpaGmTJRdc0L7ZSFtSYzANUI"

def getInnerHTML(playlistUrl):
    with sync_playwright() as pl:
        browser = pl.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(playlistUrl)
        page.get_by_role("button", name="Accept all").click()
        page.wait_for_selector("#contents")
        return page.evaluate('''() => {
            const element = document.querySelector('div#primary.style-scope ytd-section-list-renderer');
            return element.innerHTML;
        }''')

def scrapeVids(html):
    soup = bs(html, "html.parser").select(".style-scope ytd-playlist-video-renderer")
    playlist = []
    for el in soup:
        video = []
        h1 = el.select_one("a#video-title").text.strip()
        link = "https://youtube.com" + el.select_one("div#content ytd-thumbnail a").attrs['href']
        charRem = "list"
        link = link[:link.index(charRem) + (len(charRem) - 3)]
        video.append([h1, link])
        playlist.append(video)
    return playlist

def pandas_output(main_list):
    DataFrame = pd.DataFrame(main_list)
    print(DataFrame)

# def test():
# testList = scrapeVids(getInnerHTML(pl_url))
# for vid in testList:
#     for el in vid:
#         print(el[0])