# -*- coding: utf-8 -*-
from operator import index
import click
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
from nltk.tokenize import RegexTokenizer
import numpy as np
import pandas as pd
import random
SEED = 101

def make_train_test(data, test_size=0.3):
    train, test = train_test_split(data, test_size=test_size, random_state=SEED)
    return train, test

def save_file(data, output_filepath):
    data.to_csv(output_filepath, index=False)

def clean_names(name):
    tokenizer = RegexTokenizer(r'\w+')
    
    token = tokenizer.tokenize(name)
    name = ''
    
    for n in token:
        if not n.isdigit() and not n == 'rm':
            name += n
            name += ' '
    
    name = name.strip(n)
    return name

def fill_nan(data, fill=''):
    data[data.isna()] = fill
    return data

def split_category(data):
    columns = data.category_name.str.split('/', expand=True)
    for i in range(3):
        data.loc[:, f'category_{i+1}'] = columns[i]
    data.drop('category_name', axis=1, inplace=True)
    return data

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    
    data = pd.read_csv(input_filepath)
    data.loc[:, 'name'] = [clean_names(name) for name in data.name]
    data.loc[:, 'brand_name'] = fill_nan(data['branch_name'], fill='No Branch')
    data = split_category(data)
    data = data[['name', 'category_1', 'category_2', 'category_3', 'item_condition_id',
                 'brand_name', 'price', 'shipping', 'item_description']]
    
    for i in range(1, 4):
        data.loc[:, f'category_{i}'] = fill_nan(data[f'category_{i}'],
                                                fill='No category')
    
    train_data, test_data = make_train_test(data)
    train_filepath = output_filepath + '/train_data.csv'
    test_filepath = output_filepath + '/test_data.csv'
    
    save_file(train_data, train_filepath)
    save_file(test_data, test_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    main()
