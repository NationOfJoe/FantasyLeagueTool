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
        report += '<tr>'
        report += '<td>Price</td>'
        report += '<td>Efficency Average</td>'
        report += '<td>Position</td>'
        report += '<td>Team</td>'
        report += '<td>Name</td>'
        report += '</tr>'
        for mem in someteam.members:
            bgcolor = ''
            if mem.eff == someteam.mvp:
                bgcolor = "#00FF00"
            report += '<tr>'
            report += '<td bgcolor='+bgcolor + '>' + str(mem.price) + '</td>'
            report += '<td bgcolor='+bgcolor + '>' + str(mem.eff) + '</td>'
            report += '<td bgcolor='+bgcolor + '>' + mem.pos + '</td>'
            report += '<td bgcolor='+bgcolor + '>' + mem.leagueteam + '</td>'
            report += '<td bgcolor='+bgcolor + '>' + mem.name + '</td>'
            report += '</tr>'
        report += '<tr>'
        report += '<td>' + str(round(float(someteam.totalPrice), 2)) + '</td>'
        report += '<td>' + str(round(float(someteam.effeff), 2)) + '</td>'
        report += '<td></td>'
        report += '<td></td>'
        report += '<td>Total</td>'
        report += '</tr>'
        report += '</tr></table>'
    return report
