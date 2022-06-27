from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
soup = bs(page.content, 'html.parser')
temp_list = []

star_table = soup.find_all('table')
rows = star_table[7].find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

file_data = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=['Name', 'Distance (light years)', 'Mass (Jupiter mass)', 'Radius (Jupiter Radius)'])
file_data.to_csv('scraper.csv')