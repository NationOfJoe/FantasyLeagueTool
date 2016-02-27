import urllib3 as web
import re

http = web.PoolManager(10)
resp = http.urlopen("GET", 'http://basket.co.il/StatsPage_Individual.asp?c=1&sType=VAL&cYear=2016&local=0&StatsBoard=0')
frags = resp.data.decode("windows-1255")
a = frags.split('<td id="td_stats" style="width:20px;background-color:#aeaeae;"')
b = a[1].split()
pass
