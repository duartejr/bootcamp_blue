#%%
import numpy as np
from datetime import datetime
from avaliacao_modelos import *
from prep_data import load_train_test
from xgboost import XGBRegressor
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer

print('iniciado')

X_treino, y_treino, dados_teste = load_train_test()
print('dados lidos')
model = XGBRegressor(random_state=101, n_jobs=-1)

print('xgboos criado')
parameters = {'min_samples_leaf'        : [2, 4, 8, 16, 32, 64, 128],
              'min_samples_split'       : [2, 4, 8, 16, 32, 64, 128],
              'n_estimators'            : [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
              'max_depth'               : [2, 4, 8, 16, 32, 64, 128],
              'criterion'               : ['poisson']
             }
print('params')
start_time = datetime.now()
print('startado')

print('Definindo o modelo de otimização')
opt = BayesSearchCV(
    model,
    {
        'n_estimators'            : Integer(100, 1000),
        'max_depth'               : Integer(2, 128),
        'grow_policy'             : Categorical(['depthwise', 'lossguide']),
        'eta'                     : Real(0.001, 0.5, 'log-uniform'),
        'subsample'               : Real(0.001, 1.0, 'log-uniform'),
        'colsample_bytree'        : Real(0.001, 1.0, 'log-uniform'),
        
    },
    n_iter=10,
    cv=3,
    verbose=20,
    scoring='neg_mean_absolute_error'
)
print('modelo definido.')
print('Otimização do modelo XGBoost Geral\n\n')

#%%
opt.fit(X_treino, y_treino)
dados_teste['pred'] = np.exp(opt.predict((dados_teste.drop('price', axis=1))))
dados_teste.loc[dados_teste.pred < 3, 'pred'] = 3
#%%
print('\nAvaliação modelo XGBoost Geral')
print('\nAvaliação geral')
print_avaliacao(dados_teste['price'], dados_teste['pred'])
print('\nAvaliação por categoria')
avaliacao_categorica(dados_teste)

end_time = datetime.now()
print("\n\nDuration: {}".format(end_time - start_time))
#%%