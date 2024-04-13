from bs4 import BeautifulSoup
import requests

def scrapeBlah():
   #pageToScrape = requests.get("https://www.scrapethissite.com/pages/simple/")
   ebayTestScrape = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=levis+569s")
   souper = BeautifulSoup(ebayTestScrape.text, "html.parser")
   pants = souper.findAll('span', attrs={'role':'heading'})
   for pant in pants:
      if " 30x30 " in pant.text:
         print(pant.text)
      if " 30 x 30 " in pant.text:
         print(pant.text)
      if " 30 x 30" in pant.text:
         print(pant.text)
      if " 30x30" in pant.text:
         print(pant.text)
      if " 30W x 30L " in pant.text:
         print(pant.text)

scrapeBlah()