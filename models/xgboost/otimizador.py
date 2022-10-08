from sklearn.model_selection import RandomizedSearchCV
from avaliacao_modelos import *

def optmize(X_train, y_train, estimator, param_distributions, cv=5,
            n_iter=10, verbose=True, file=None):
    print('Init RodomizedSearchCV')
    
    random_scv = RandomizedSearchCV(estimator=estimator,
                                    param_distributions=param_distributions,
                                    cv=cv,
                                    n_iter=n_iter,
                                    verbose=verbose)
    random_scv.fit(X_train, y_train)
    
    print(" Results from Random Search ", file=file)
    print("\n The best estimator across ALL searched params:\n", random_scv.best_estimator_, file=file)
    print("\n The best score across ALL searched params:\n", random_scv.best_score_, file=file)
    print("\n The best parameters across ALL searched params:\n", random_scv.best_params_, file=file)
    
    return random_scv