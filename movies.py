import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('movies.csv')

    print(df['duration'].dtype)
    print(df['rating'].dtype)
    print(df['votes'].dtype)

    df_cleaned = df.dropna().copy()
    df_cleaned['rating_weighted'] = df_cleaned['rating'] * np.log10(df_cleaned['votes'])

    df_filtered = df_cleaned[(df_cleaned['year'] > 2000) & (df_cleaned['duration'] > 120)]
    df_head = df_filtered.sort_values('rating_weighted', ascending=False).head(10)
    print(df_head)

    df_head['genre'] = df_head['genre'].apply(lambda x: [i.strip() for i in x.split(',')])
    genre_counts = df_head['genre'].explode().value_counts()
    print(genre_counts)


if __name__ == '__main__':
    main()