import pandas as pd
import requests

url = "https://restcountries.com/v3.1/all"
src = requests.get(url)
data = src.json()

countries = []
for country in data:
    try:
        var = {
            "name": country["name"]["common"],
            "region": country.get("region", None),
            "subregion": country.get("subregion", None),
            "area": country.get("area", None),
            "population": country.get("population", None),
            "languages": country.get('languages', {}),
            "independent": country.get("independent", None),
        }
        countries.append(var)
    except KeyError:
        continue
df = pd.DataFrame(countries)

df = df.dropna(subset=["area", "population", "languages"])
df['pop_density'] = df['population'] / df['area']
df['num_languages'] = df['languages'].apply(lambda x: len(x))

mean_languages = df.groupby('subregion')['num_languages'].mean()
df_sorted = df.sort_values(by='pop_density', ascending=False).copy()
print(df_sorted.head(10))
print(mean_languages)