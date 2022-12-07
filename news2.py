import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://www.google.com/search?q=dainik+jagran&rlz=1C1CHBF_enIN1025IN1025&oq=danik&aqs=chrome.1.69i57j0i10i131i433i512l2j0i10i512j0i10i131i433i512l2j0i131i433j0i10i131i433i512j0i131i433j0i10i512.2168j0j15&sourceid=chrome&ie=UTF-8")
    topics = await page.querySelectorAll(".kno-rdesc span")
    for topic in topics:
        title = await topic.getProperty("textContent")
    # print the article titles
        print(await title.jsonValue())

    
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
