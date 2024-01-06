import requests
from bs4 import BeautifulSoup

def fetch_country_details():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming the country details are in a table with class "table"
        table = soup.find('table', {'class': 'table'})

        if table:
            # Extracting data from the table
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skip the header row
                columns = row.find_all('td')
                country = columns[0].get_text(strip=True)
                capital = columns[1].get_text(strip=True)
                population = columns[2].get_text(strip=True)
                print(f"Country: {country}, Capital: {capital}, Population: {population}")

        else:
            print("Table not found on the page.")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_country_details()
