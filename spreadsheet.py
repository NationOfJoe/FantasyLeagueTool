import json
import gspread
import random
import itertools
from oauth2client.client import SignedJwtAssertionCredentials


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


class team:
    def __init__(self):
        self.totalPrice = 0.0
        self.members = []
        self.totalratio = 0.0
        self.totaleff = 0.0

    def calc(self):
        self.mvp = 0.0
        for member in self.members:
            self.totalPrice = self.totalPrice + member.price
            self.totalratio = self.totalratio + member.ratio
            self.totaleff = self.totaleff + member.eff + member.teamratio
            if member.eff > self.mvp:
                self.mvp = member.eff
        self.effeff = self.mvp + self.totaleff

    def checktwoplayersperteam(self):
        clubsinteam = []
        for member in self.members:
            clubsinteam.append(member.leagueteam)
        afterfirst = list(set(clubsinteam))
        aftersecond = list(set(afterfirst))
        if afterfirst.__len__() == aftersecond.__len__():
            result = 'OK'
        else:
            result = 'dups'
        return result

class club:
    def __init__(self, ratio, losses, wins, name):
        self.name = name
        self.ratio = ratio
        self.losses = losses
        self.wins = wins


teams = []
secondforward = secondCenter = firstCenter = firstforward = ''
firstguard = secondguard = thirdguard = thirdforward = ''
json_key = json.load(open('D:\\\\googleSpreadsheetauth.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
wks = gc.open("fantasyleague")
worksheet_list = wks.worksheets()
sh = wks.sheet1
sh2 = wks.get_worksheet(1)
teamtablepos = sh2.get_all_values()
clubs = []
for aclub in teamtablepos:
    aclub[3] = aclub[3].rstrip()
    aclub[3] = aclub[3].lstrip()
    clubs.append(club(float(aclub[0]), int(aclub[1]), int(aclub[2]), aclub[3]))
players = []
centers = []
guards = []
forwards = []
rawplayers = sh.get_all_values()
for rawplayer in rawplayers:
    players.append((player(rawplayer[5], float(rawplayer[2]), int(rawplayer[1]), rawplayer[3], float(rawplayer[0]), rawplayer[4])))
for inplayer in players:
    inplayer.name = inplayer.name.lstrip()
    inplayer.name = inplayer.name.rstrip()
    inplayer.leagueteam = inplayer.leagueteam.lstrip()
    inplayer.leagueteam = inplayer.leagueteam.rstrip()
    inplayer.getratiobyclub(clubs)
    if inplayer.pos == 'גארד' :
        guards.append(inplayer)
    if inplayer.pos == 'סנטר' :
        centers.append(inplayer)
    if inplayer.pos == 'פורוורד' :
        forwards.append(inplayer)
for _ in itertools.repeat(None, 7500):
    x = team()
    while firstCenter == secondCenter:
        firstCenter = random.choice(centers)
        secondCenter = random.choice(centers)
    while firstforward == secondforward or firstforward == thirdforward or secondforward == thirdforward:
        firstforward = random.choice(forwards)
        secondforward = random.choice(forwards)
        thirdforward = random.choice(forwards)
    while firstguard == secondguard or firstguard == thirdguard or secondguard == thirdguard:
        firstguard = random.choice(guards)
        secondguard = random.choice(guards)
        thirdguard = random.choice(guards)
    x.members.append(firstCenter)
    x.members.append(secondCenter)
    x.members.append(firstguard)
    x.members.append(secondguard)
    x.members.append(thirdguard)
    x.members.append(firstforward)
    x.members.append(secondforward)
    x.members.append(thirdforward)
    x.calc()
    secondforward = secondCenter = firstCenter = firstforward = ''
    firstguard = secondguard = thirdguard = thirdforward = ''
    if x.totalPrice <= 470 and x.totalratio > 1.3 and x.effeff > 100:
        dup = x.checktwoplayersperteam()
        if dup == 'OK':
            teams.append(x)
teams.sort(key=lambda y: y.totaleff, reverse=True)
print("Great success")