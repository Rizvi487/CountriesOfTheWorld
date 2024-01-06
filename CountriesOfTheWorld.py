from requests_html import HTMLSession

def fetch_country_details():
    s = HTMLSession()
    url = 'https://www.scrapethissite.com/pages/simple/'
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    })
    # print(r.html.find('title',first=True).text)
    if r.status_code == 200:
        countries = r.html.find('div.row div.col-md-4.country h3.country-name')
        if countries:
            for country in countries:
                print(country.text)
        else:
            print("No elements found.")


        capitals = r.html.find('div.row div.col-md-4.country div.country-info span.country-capital')
        if capitals:
            for capital in capitals:
                print(capital.text)
        else:
            print("No Capitals Found.")

        population = r.html.find('div.row div.col-md-4.country div.country-info span.country-population')
        if population:
            for populate in population:
                print(populate.text)
        else:
            print("No Population Found")

        areas = r.html.find('div.row div.col-md-4.country div.country-info span.country-area')
        if areas:
            for area in areas:
                print(area.text)
        else:
            print("No Area Found")

    else:
        print(f"Failed to fetch the page. Status code: {r.status_code}")

if __name__ == "__main__":
    fetch_country_details()
