import pandas as pd
from pathlib import Path

data_folder = Path('data')
dfs = []

for file in data_folder.glob('*.csv'):
    df = pd.read_csv('./data/daily_sales_data_0.csv')
    # filter for pink morsel
    df = df[df['product'] == 'pink morsel']

    # convert to correct type
    df['quantity'] = df['quantity'].astype(int)
    df['price'] = df['price'].str.replace('$', '').astype(float)

    # calculate sales for each row
    df['sales'] = df['quantity'] * df['price']

    # select needed columns
    df = df[['sales', 'date', 'region']]

    # add df of each csv file after processing to dfs list
    dfs.append(df)

# combine 3 dfs together
final_df = pd.concat(dfs, ignore_index=True)

# save it into a single formatted file
final_df.to_csv('formatted_sales_data.csv', index=False)

print(final_df)
