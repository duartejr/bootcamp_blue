#%%
from unicodedata import category
from prep_data import *
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from avaliacao_modelos import *
from glob import glob
import pickle
import os

tfidfs = glob('../data/processed/xgboost/*.pickle')
dados_treino_file = '../data/processed/xgboost/dados_treino_xgboost_categorizado.csv'
#%%
dados_treino = pd.read_csv(dados_treino_file)
#%%


#%%
modelos = {}

for tfidf_file in tfidfs:
    category = tfidf_file.split('/')[-1].split('.')[0]
    print(category)
    if not os.path.exists(f'modelo_{category}.pickle'):
        print('modeling:', category)
        with open(tfidf_file, 'rb') as pickle_file:
            xgbr = XGBRegressor(random_state=101,
                                n_jobs=-1)
            tfidf = pickle.load(pickle_file)
            y_treino = np.log(dados_treino.query(f'col_att == "{category}"')['price'])
            modelo = BayesSearchCV(xgbr,
                                            {
                                                'n_estimators'     : Integer(100, 1000),
                                                'max_depth'        : Integer(2, 128),
                                                'grow_policy'      : Categorical(['depthwise', 'lossguide']),
                                                'eta'              : Real(0.001, 0.5, 'log-uniform'),
                                                'subsample'        : Real(0.001, 1.0, 'log-uniform'),
                                                'colsample_bytree' : Real(0.001, 1.0, 'log-uniform'),
                                            },
                                            n_iter=20,
                                            cv=3,
                                            verbose=2,
                                            scoring='neg_mean_absolute_error'
                                            )
            modelo.fit(tfidf, y_treino)

            with open(f'modelo_{category}.pickle', 'wb') as handle:
                pickle.dump(modelo, handle, protocol=pickle.HIGHEST_PROTOCOL)
# %%
