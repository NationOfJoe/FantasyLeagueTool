import requests
from bs4 import BeautifulSoup
import html


def createHTMLtablereport(teams):
    report = '<p>Suggested Teams:</p>'
    idx = 1
    for someteam in teams:
        team_header = r'Team {2} price {0} and total eff {1}'.format(someteam.totalPrice,
                                                                     str(round(float(someteam.effeff), 2)), str(idx))
        idx = idx + 1
        report += '<p>'+team_header + '</p><table border="1">'
        for mem in someteam.members:
            player_name = mem.name
            report += '<td>' + player_name + '</td>'
        report += '</tr></table>'
    return report
