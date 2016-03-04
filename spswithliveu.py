import random
import itertools
import getPlayervalue
import gethttpdata
import sys


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

def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(s.encode('cp1255').decode(sys.stdout.encoding))
        else:
            print(s.encode('utf8'))

inp = getPlayervalue.inputs()
inp.calc_inputs(sys.argv)
teams = []
secondforward = ''
secondCenter = ''
firstCenter = ''
firstforward = ''
firstguard = ''
secondguard = ''
thirdguard = ''
thirdforward = ''
clubs = getPlayervalue.get_league_table()
players = []
centers = []
guards = []
forwards = []
players = getPlayervalue.fill_player_list()
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
for _ in itertools.repeat(None, inp.iterations):
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
    secondforward = ''
    secondCenter = ''
    firstCenter = ''
    firstforward = ''
    firstguard = ''
    secondguard = ''
    thirdguard = ''
    thirdforward = ''
    if x.totalPrice <= 470 and x.totalratio > inp.mintotratio and x.effeff > inp.effcutoff:
        dup = x.checktwoplayersperteam()
        if dup == 'OK':
            teams.append(x)
teams.sort(key=lambda y: y.totaleff, reverse=True)
report = gethttpdata.createHTMLtablereport(teams)
filename = 'd:\git\qqq.html'
f = open(filename, 'w', encoding='utf_8')
print(report, file=f)
f.close()
safeprint(report)
