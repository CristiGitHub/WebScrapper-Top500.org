from bs4 import BeautifulSoup
import pprint as pp
import urllib
from urllib.request import urlopen
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

results = []
anii = []
for an in range(1993, 2021):
    url = "https://www.top500.org/lists/top500/" + str(an) + '/' + '11' + '/'
    req = urllib.request.urlretrieve(url, "source.html")
    page = 'source.html'
    soup = BeautifulSoup(open(page, encoding="utf-8"), 'lxml')
    headings = soup.find_all('tr')

    med = 0
    mr = 0
    for head in headings:
        mr = mr + 1
        if (mr <= 4):
            pret = head.find_all('td')
            nr = 0
            for price in pret:
                nr = nr + 1
                if (nr == 4):
                    pr = float(price.text.strip().replace(',', ''))
                    med = med + pr
    if an <= 2004:
        med = med / 1000
    results.append(med / 3)
    anii.append(an + 0.5)
for an in range(1993, 2021):
    url = "https://www.top500.org/lists/top500/" + str(an) + '/' + '06' + '/'
    req = urllib.request.urlretrieve(url, "source.html")
    page = 'source.html'
    soup = BeautifulSoup(open(page, encoding="utf-8"), 'lxml')
    headings = soup.find_all('tr')

    med = 0
    mr = 0
    for head in headings:
        mr = mr + 1
        if (mr <= 4):
            pret = head.find_all('td')
            nr = 0
            for price in pret:
                nr = nr + 1
                if (nr == 4):
                    pr = float(price.text.strip().replace(',', ''))
                    med = med + pr
    if an <= 2004:
        med = med / 1000
    results.append(med / 3)
    anii.append(an)

z = np.polyfit(anii, results, 2)
f = np.poly1d(z)

x_new = np.linspace(anii[0], anii[-1], 50)
y_new = f(x_new)

plt.plot(anii,results,'.',)
plt.grid(color='r', linestyle='-', linewidth=0.2)
plt.show()