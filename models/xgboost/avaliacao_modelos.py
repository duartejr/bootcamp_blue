import pandas as pd
from sklearn import metrics

def calc_metricas(obs, pred):
    r2 = metrics.r2_score(obs, pred).round(3)
    mape = (100 * metrics.mean_absolute_percentage_error(obs, pred)).round(3)
    mae = metrics.mean_absolute_error(obs, pred).round(2)
    rmse = (metrics.mean_squared_error(obs, pred)**0.5).round(2)
    msle = metrics.mean_squared_log_error(obs, pred).round(3)
    
    return [r2, mape, mae, rmse, msle]


def print_avaliacao(obs, pred, file=None):
    print('R² = %.3f' % metrics.r2_score(obs, pred), file=file)
    print('MAPE = %.3f %%' % (100 * metrics.mean_absolute_percentage_error(obs, pred)), file=file)
    print('MAE = U$S %.2f' % (metrics.mean_absolute_error(obs, pred)), file=file)
    print('RMSE = U$S %.2f' % metrics.mean_squared_error(obs, pred)**0.5, file=file)
    print('MSLE = %.3f' % metrics.mean_squared_log_error(obs, pred), file=file)
    

def avaliacao_categorica(dados_teste, file=None):
    avaliacoes = {}

    for categoria in dados_teste.category_1.unique():
        dados_cat = dados_teste.query(f'category_1 == {categoria}')
        avaliacoes[categoria] = calc_metricas(dados_cat['price'],
                                              dados_cat['pred'])

    avaliacoes = pd.DataFrame(avaliacoes,
                              index=['R²', 'MAPE', 'MAE', 'RMSE', 'MSLE'])

    avaliacoes.columns = ['Women', 'Men', 'Vintage & Collectibles', 'Electronics',
                        'Beauty', 'Kids', 'Other', 'Home', 'Sports & Outdoors',
                        'Handmade', 'No category']

    print(avaliacoes.to_string(), file=file)