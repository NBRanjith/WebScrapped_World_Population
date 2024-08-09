from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'

requests.get(url)

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

#soup.find_all('table')

table = soup.find_all('table')

#soup.find_all('th')

world_column = soup.find_all('th')

world_column_title = [columns.text for columns in world_column ]

#print(world_column_title)


df = pd.DataFrame(columns = world_column_title)

#df
#soup.find_all('td')

world_rows = soup.find_all('tr')

for rows in world_rows[1:]:
    row_data = rows.find_all('td')
    individual_data = [data.text for data in row_data]

    length = len(df)
    df.loc[length] = individual_data

df

df.to_csv(r'D:\MASTERS\pyth\Projects\4th Project\world_population_scrapped.csv', index = False)