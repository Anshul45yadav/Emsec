import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://en.wikipedia.org/wiki/Tiger")
    
    # create a screenshot of the page and save it
    await page.screenshot({"path": "tiger.png"})
    data = await page.evaluate('''
        () => {
            const content=document.querySelectorAll('.mw-parser-output p')
            const g=Array.from(content).map(para =>para.innerHTML)
            return g
        }
    ''')
    alldata = ''.join(data)
    print(alldata)
    soup = BeautifulSoup(alldata)
    text = soup.get_text()
    print(text)
   
    
    # close the browser
    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")
