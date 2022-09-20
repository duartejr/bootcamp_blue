# -*- coding: utf-8 -*-
from operator import index
import click
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd
SEED = 101

def make_train_test(data, test_size=0.3):
    train, test = train_test_split(data, test_size=test_size, random_state=SEED)
    return train, test

def save_file(data, output_filepath):
    data.to_csv(output_filepath, index=False)

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
