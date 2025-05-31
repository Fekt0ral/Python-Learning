import requests
import pandas as pd
from bs4 import BeautifulSoup

data = requests.get('https://www.scrapethissite.com/pages/simple/').text
soup = BeautifulSoup(data, "html.parser")

rows = []

for row in soup.find_all("div", class_='col-md-4 country'):
    country = row.find("h3", class_="country-name").text.strip()
    capital = row.find("span", class_="country-capital").text.strip()
    population = row.find("span", class_="country-population").text.strip()
    area = row.find("span", class_="country-area").text.strip()
    rows.append({"Country": country, "Capital": capital, "Population": population, "Area": area})

data = pd.DataFrame(rows)

data['Population'] = pd.to_numeric(data['Population'], errors='coerce')
data['Area'] = pd.to_numeric(data["Area"], errors="coerce")

data["Density"] = data["Population"] / data["Area"]
print(f"The country with the highest population density: {data.loc[data['Density'].idxmax(), 'Country']}")

print(f"Average area of countries: {data['Area'].mean():.2f}")

print()

print(data.head(5))