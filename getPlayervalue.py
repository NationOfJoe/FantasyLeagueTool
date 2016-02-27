import requests
from bs4 import BeautifulSoup
import html

class player:
    def __init__(self, name, peff, pprice, ppos, pratio, leagueteam):
        self.name = name
        self.leagueteam = leagueteam
        self.pos = ppos
        self.price = pprice
        self.ratio = pratio
        self.eff = peff
        self.teamratio = 0.0

    def getratiobyclub(self, clubs):
        for someclub in clubs:
            if someclub.name == self.leagueteam:
                self.teamratio = someclub.ratio * 5


def fill_player_list():
    players = []
    statsurl = 'http://basket.co.il/Game/search.asp?mode=2'
    r = requests.get(statsurl)
    sitedata = r.content.decode('cp1255')
    soup = BeautifulSoup(sitedata, 'html.parser')
    agg = soup.find_all('tr', attrs={'style': 'border-bottom:Solid 1px #ccc;'})
    for row in agg:
        segs = row.text.split()
        if segs.__len__() == 7:
            price = float(segs[0])
            eff = float(segs[1])
            pos = segs[2]
            name = segs[3] + ' ' + segs[4]
            team = segs[5] + ' ' + segs[6]
            ratio = (float(eff)/float(price))
            players.append(player(name, eff, price, pos, ratio, team))
    return players
