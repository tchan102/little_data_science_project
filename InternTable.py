import re
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import date
import requests
import os


class InternTable:
    url = "https://github.com/SimplifyJobs/Summer2024-Internships"
    local_directory = "records/"
    dataFrame = None

    def __init__(self) -> None:
        file_names = os.listdir(InternTable.local_directory)
        if f"{date.today()}.csv" not in file_names:
            InternTable.dataFrame = self.__generateDF()
            self.__generateCSV(InternTable.dataFrame)
        else:
            InternTable.dataFrame = pd.read_csv(InternTable.local_directory + str(date.today()) +'.csv')

    def getDataFrame(self):
        return InternTable.dataFrame           
            
    def __generateDF(self):
        content = self.__praseOnline(InternTable.url)
        # content = pariseLocally()
        soup = BeautifulSoup(content, 'html.parser')
        rows = soup.find_all('tr')
        columns = self.__turnRowsToColumns(rows)
        return self.__fixTheIssueForEmptyCompanyData(pd.DataFrame(
        {
            'Company': columns[0],
            'Title': columns[1],
            'Location': columns[2],
            'Month': columns[3],
            'Year': columns[4]
        }))
    
    def __praseOnline(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return str(soup.find('article', class_='markdown-body').find('tbody')).replace('<tbody>','').replace('</tbody>','')
        except requests.RequestException as e:
            print(f"Error fetching the web page: {e}")
            return None

    def __praseLocally(self, filename):
        content = ""
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f'The file {filename} does not exist.')
        return content

    def __turnRowsToColumns(self,rows):
        companies = np.array([])
        titles = np.array([])
        locations = np.array([])
        months = np.array([])
        years = np.array([])
        for row in rows: 
            company, title, location, month, year = self.__organizeOneEntry(row)
            companies = np.append(company, companies)
            titles = np.append(title, titles)
            locations = np.append(location, locations)
            months = np.append(month, months)
            years = np.append(year, years)
        return companies, titles, locations, months, years

    def __organizeOneEntry(self,row):
        f = lambda date_string: re.sub(r'\d+', '', date_string).strip()

        months2024 = ['Jan', 'Feb', 'Mar']

        months2023 = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        entry = row.find_all('td')
        entry_text = [cell.get_text(strip=True) for cell in entry]
        entry_text.pop(3)
        month = f(entry_text.pop())
        if month in months2023:
            entry_text.extend([month, 2023])
        elif month in months2024:
            entry_text.extend([month, 2024])
        return entry_text
    
    def __fixTheIssueForEmptyCompanyData(self, df):
        df['Company'].replace('↳', np.nan, inplace=True)

        df['Company'] = df['Company'].bfill()
        return df

    def __generateCSV(self, df):
        df.to_csv(f'{InternTable.local_directory}{date.today()}.csv', index=False)
