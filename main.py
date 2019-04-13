import pandas as pd
import re

import nltk


DATA_DIR  = './data/ratemyprofessors.csv';

test_string = ["I would recommend this to be proceeded with a sequel as the overall sentiment is positive."]

categories = ['POS'	,'ID' 'PosScore',	'NegScore'	,'SynsetTerms',	'Gloss'];


def get_data():
    df = pd.read_csv(DATA_DIR)
    print(df)
    return df



if __name__ == "__main__":
    get_data()
