from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

data_table = soup.find('table', class_= "wikitable sortable")

data_table_headers = [ title.text.strip() for title in data_table.find_all('th')]

data_frame = pd.DataFrame(columns=data_table_headers)

column_data = data_table.find_all('tr')

for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [ data.text.strip() for data in row_data]

    if len(individual_row_data) <= 0:
        continue
    
    length = len(data_frame)
    data_frame.loc[length] = individual_row_data
    pass

data_frame.to_csv(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/web-scrapper/Companies.csv", index = False)

