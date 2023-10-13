from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

# pl_url = "https://youtube.com/playlist?list=PLKq6LCtE6MpaGmTJRdc0L7ZSFtSYzANUI"

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

def scrapeUrls(html):
    urls = []
    for vid in bs(html, "html.parser").select(".style-scope ytd-playlist-video-renderer"):
        link = "https://youtube.com" + vid.select_one("div#content ytd-thumbnail a").attrs['href']
        charRem = "list"
        link = link[:link.index(charRem) + (len(charRem) - 3)]
        urls.append(link)
    return urls

def pandas_output(main_list):
    DataFrame = pd.DataFrame(main_list)
    print(DataFrame)

def test():
    testList = scrapeUrls(getInnerHTML("https://www.youtube.com/playlist?list=PLKq6LCtE6MpYbWinZS-pOXAUZW8FpPpMF"))
    for i in testList:
        print(i)
