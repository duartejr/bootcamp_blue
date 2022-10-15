#%%
from tabnanny import verbose
import numpy as np
from datetime import datetime
from otimizador import optmize
from avaliacao_modelos import *
from prep_data import load_train_test
from scipy.stats import randint as sp_randInt
from scipy.stats import uniform as sp_randFloat
from sklearn.ensemble import RandomForestRegressor
from skopt import BayesSearchCV

X_treino, y_treino, dados_teste = load_train_test()

rfr = RandomForestRegressor(n_jobs=-1,
                            random_state=101,
                            warm_start=True,
                            criterion='poisson')

parameters = {'min_samples_leaf'        : [2, 4, 8, 16, 32, 64, 128],
              'min_samples_split'       : [2, 4, 8, 16, 32, 64, 128],
              'n_estimators'            : [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
              'max_depth'               : [2, 4, 8, 16, 32, 64, 128],
              'criterion'               : ['poisson']
             }
start_time = datetime.now()

opt = BayesSearchCV(
    rfr,
    {
        'min_samples_leaf'        : (2, 128),
        'min_samples_split'       : (2, 128),
        'n_estimators'            : (100, 1000),
        'max_depth'               : (2, 128),
    },
    n_iter=10,
    cv=3,
    verbose=20
)

print('Otimização do modelo Random Forest\n\n')

# model = optmize(X_treino,
#                 y_treino,
#                 rfr, parameters,
#                 cv=3,
#                 n_iter=20,
#                 verbose=20,
#                 file=f)
    
#%%
opt.fit(X_treino, y_treino)
dados_teste['pred'] = np.exp(opt.predict((dados_teste.drop('price', axis=1))))
dados_teste.loc[dados_teste.pred < 3, 'pred'] = 3
#%%
print('\nAvaliação modelo RandomForest')
print('\nAvaliação geral')
print_avaliacao(dados_teste['price'], dados_teste['pred'])
print('\nAvaliação por categoria')
avaliacao_categorica(dados_teste)

end_time = datetime.now()
print("\n\nDuration: {}".format(end_time - start_time))
#%%