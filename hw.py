import itertools
import sys

import pandas as pd

SUPPORT_S = 1
df = pd.read_csv('online_retail.csv', sep=';', nrows=100)
df: pd.DataFrame = df[df['CustomerID'].notna()]
print(df)
customer_bucket = {}
stocks_count = {}
unique_stocks = set()


for index, row in df.iterrows():
    cid = int(row['CustomerID'])
    stock = row['StockCode']
    unique_stocks.add(stock)

    if stock in stocks_count:
        stocks_count[stock] += 1
    else:
        stocks_count[stock] = 0

    if cid in customer_bucket:
        customer_bucket[cid]['stocks'].append(stock)
    else:
        customer_bucket[cid] = {
            'stocks': [stock]
        }

print('unique stocks len', len(unique_stocks))
unique_stocks = list(unique_stocks)
combinations_count = {}
unique_combinations = set()

all_hashes = []
all_hashes2 = []

hash_1 = {}
hash_2 = {}

for customer in customer_bucket.keys():
    customer_hashes = []

    combinations_of_stocks = []

    for subset in itertools.combinations(customer_bucket[customer]['stocks'], 2):
        combinations_of_stocks.append(subset)
        if subset in combinations_count:
            combinations_count[subset] += 1
        else:
            combinations_count[subset] = 0
        unique_combinations.add(subset)

        i = unique_stocks.index(subset[0])
        j = unique_stocks.index(subset[1])
        result = (i + j) % len(unique_stocks)
        all_hashes.append(result)

        if result in hash_1:
            hash_1[result].append(subset)
        else:
            hash_1[result] = [subset]

        result2 = (i + 2 * j) % len(unique_stocks)
        all_hashes2.append(result2)

        if result2 in hash_2:
            hash_2[result2].append(subset)
        else:
            hash_2[result2] = [subset]

    print(combinations_of_stocks)

    # break

for i in hash_1:
    comb_array = hash_1[i]
    for idx, j in enumerate(comb_array):
        if combinations_count[j] < SUPPORT_S:
            del comb_array[idx]
    hash_1[i] = comb_array

for i in hash_2:
    comb_array = hash_2[i]
    for idx, j in enumerate(comb_array):
        if combinations_count[j] < SUPPORT_S:
            del comb_array[idx]
    hash_2[i] = comb_array

final_count_stock = {}
print(f"\nCOMBINATIONS BIGGER THAN SUPPORT S\n")
for i in unique_combinations:
    if stocks_count[i[0]] > SUPPORT_S and stocks_count[i[1]] > SUPPORT_S:
        print(i)

