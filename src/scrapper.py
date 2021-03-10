import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse

class aavsoScrapper:
    def __init__(self):
        pass


    def doTheFuckingJob(self,args):
        print("Welcome to aavsoscrapper library.")
        URL = 'https://www.aavso.org/'
        page = req.get(URL)
        soup = bs(page.content, 'html.parser')
        form_build_id = soup.find('input', {"name":"form_build_id"})['value']
        form_id = soup.find('input', {"name":"form_id"})['value']
        op = "Create a finder chart"
        auid = args[0]
        r = req.post('https://www.aavso.org/', data = 
        {
            'form_build_id':form_build_id,
            'form_id':form_id,
            'op':op,
            'auid':auid
        })

        soup = bs(r.content, 'html.parser')

        chart_href = soup.find(lambda tag:tag.name=="a" and "Photometry Table for This Chart" in tag.text)['href']
        chart_url = urllib.parse.urljoin(r.url, chart_href)

        img_src = soup.select('div > a > img')[0]['src']
        img_url = urllib.parse.urljoin(r.url, img_src)

        
        chart_page = req.get(chart_url)
        soup = bs(chart_page.content, 'html.parser')
        chart_table = soup.find(lambda tag:tag.name=="table" and "AUID" in tag.text)
        rows  = chart_table.select('tbody > tr')
        comparisonStars = []
        for row in rows:
            cells = row.find_all('td')
            cs = ComparisonStar(cells[0].text,
                                cells[1].text,
                                cells[2].text,
                                cells[3].text,
                                cells[4].text,
                                cells[5].text,
                                cells[6].text)
            comparisonStars.append(cs)
        img = req.get(img_url).content


class ComparisonStar:
    def __init__(self,auid,ra,dec,label,v,bv,comment):
        self.auid = auid
        self.ra = ra
        self.dec = dec
        self.label = label
        self.v = v
        self.bv = bv
        self.comment = comment