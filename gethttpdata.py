import requests
from bs4 import BeautifulSoup
import html

class player:
    def __init__(self, name, peff, leagueteam):
        self.name = name
        self.leagueteam = leagueteam
        self.peff = peff


players = []
pages = range(6)
for page in pages:
    statsurl = 'http://basket.co.il/StatsPage_Individual.asp?c='+ str(page + 1) +'&sType=VAL&cYear=2016&local=0&StatsBoard=0'
    r = requests.get(statsurl)
    sitedata = r.content.decode('cp1255')
    soup = BeautifulSoup(sitedata, 'html.parser')
    agg = soup.find_all('td', attrs={'id': 'td_stats'})
    for idx, p in enumerate(agg):
        if (idx + 1) % 20 == 2:
            name = p.text
        if (idx + 1) % 20 == 3:
            team = p.text
        if (idx + 1) % 20 == 0:
            eff = p.text
            players.append(player(name, eff, team))
pass