
import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://indianexpress.com/")

    # create a screenshot of the page and save it
    
    # close the browser

    topics = await page.querySelectorAll(".t-elecblock-right h1")
    for topic in topics:
        title = await topic.getProperty("textContent")
           # print the article titles
        print(await title.jsonValue())



    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
