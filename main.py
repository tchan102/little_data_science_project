import matplotlib.pyplot as plt
from InternTable import InternTable

def getAllTitlesFromACompany(df, company_name):
    company_positions = df[df['Company'] == company_name]

    return company_positions['Title'].unique()

def plotShowAllMonthsRanked(df):
    df['MonthYear'] = df['Month'].astype(str) + '-' + df['Year'].astype(str)
    grouped = df.groupby('MonthYear').size().reset_index(name='Count').sort_values(by='Count', ascending=False)

    grouped.plot(kind='bar', x='MonthYear', y='Count', color='skyblue', figsize=(12, 6), legend=False)
    plt.title('All Month-Year Combinations by Count')
    plt.xlabel('Month-Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.show()

def plotShowTopNCompanies(df, n = 5):
    groupedByCompany = df.groupby('Company').size()

    top_n_companies = groupedByCompany.sort_values(ascending=False).head(n)
    top_n_companies = top_n_companies[::-1]
    top_n_companies.plot(kind='barh', figsize=(10, 6), color='skyblue')
    plt.title(f'Top {n} Companies by Count')
    plt.xlabel('Count')
    plt.ylabel('Company')
    plt.tight_layout()
    plt.show()

def totalNumberOfInterns(df):
    return len(df)

def allInternsInThatMonthAndYear(df, month, year):
    return df[(df['Month'] == month) & (df['Year'] == year)]

if __name__ == "__main__":
    interns = InternTable()
    df = interns.getDataFrame()
    print(totalNumberOfInterns(df))