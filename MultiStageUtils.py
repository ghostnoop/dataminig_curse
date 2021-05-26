import itertools
import sys

import pandas as pd

SUPPORT_S = 1


def get_data():
    df = pd.read_csv('online_retail.csv', sep=';', nrows=100)
    df: pd.DataFrame = df[df['CustomerID'].notna()]
    return df


def get_index_from_dict(dictionary):
    return len(dictionary.keys())+1
