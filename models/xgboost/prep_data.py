
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


def encoder(dados_treino, dados_teste, columns=['category_1',
                                                'category_2',
                                                'category_3',
                                                'brand_name']):
    for col in columns:
        encoder = LabelEncoder()
        dados_treino.loc[:, col] = encoder.fit_transform(dados_treino[col])
        dic_encoder = dict(zip(encoder.classes_,
                               encoder.transform(encoder.classes_)))
        dados_teste.loc[:, col] = dados_teste[col].\
                                  map(dic_encoder).\
                                  fillna(-1)
    
    return dados_treino, dados_teste

def load_data(encoder_data=False, columns_encoder=None):
    dados_treino = pd.read_csv('../data/processed/train_data.csv')
    dados_teste = pd.read_csv('../data/processed/test_data.csv')

    if encoder_data:
        dados_treino, dados_teste = encoder(dados_treino,
                                            dados_teste,
                                            columns=columns_encoder)
    
    return dados_treino, dados_teste

def load_train_test(columns=['category_1',        'category_2', 'category_3',
                             'brand_name', 'item_condition_id',   'shipping'],
                    target='price',
                    encoder_data=True,
                    columns_encoder=['category_1', 'category_2', 'category_3', 'brand_name'],
                    processing_text_cols=False):
    dados_treino, dados_teste = load_data(encoder_data=encoder_data,
                                          columns_encoder=columns_encoder)
    if processing_text_cols:
        dados_treino, dados_teste = prep_text_columns(dados_treino, dados_teste)
        return dados_treino, dados_teste
    
    #X_treino = dados_treino[columns]
    dados_teste = dados_teste[columns + [target]]
    #y_treino = np.log(dados_treino[target])
    
    return dados_treino, dados_teste

def prep_text(text):
    try:
        tokens = word_tokenize(text)
        words = [word.lower() for word in tokens if word.isalpha()]
        words = [word for word in words if not word in stop_words]
    except:
        return None
    return ' '.join(words)

def prep_text_columns(X_treino, dados_teste):
    X_treino.loc[:, 'name'] = X_treino.apply(lambda x: prep_text(x['name']), axis=1)
    X_treino.loc[:, 'item_description'] = X_treino.apply(lambda x: prep_text(x['item_description']), axis=1)
    X_treino['comb_name_description'] = X_treino['name'] + ' ' + X_treino['item_description']
    # dados_treino.dropna(inplace=True)

    #dados_teste = dados_teste[['category_1', 'name', 'item_description', 'price']]
    dados_teste.loc[:, 'name'] = dados_teste.apply(lambda x: prep_text(x['name']), axis=1)
    dados_teste.loc[:, 'item_description'] = dados_teste.apply(lambda x: prep_text(x['item_description']), axis=1)
    dados_teste['comb_name_description'] = dados_teste['name'] + ' ' + dados_teste['item_description']
    
    return X_treino, dados_teste

def set_col_regression(dados_treino, dados_teste):
    dados_treino['col_att'] = dados_treino['category_1'] + '-' + dados_treino['shipping'].astype(str)
    dados_treino1 = dados_treino[['col_att', 'comb_name_description', 'price']]
    dados_treino1.dropna(inplace=True)

    dados_teste['col_att'] = dados_teste['category_1'] + '-' + dados_teste['shipping'].astype(str)
    dados_teste1 = dados_teste[['col_att', 'comb_name_description', 'price']]
    dados_teste1.dropna(inplace=True)
    
    return dados_treino1, dados_teste1