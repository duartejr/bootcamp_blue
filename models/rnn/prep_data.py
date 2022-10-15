from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class PrepData():

    def __init__(self,
                 features=['brand_name', 'category_1', 'category_2', 'category_3', 'name', 'item_description'],
                 max_lengths=[6, 3, 5, 7, 17, 245]):
        self.features = features
        self.max_lengths = max_lengths
        self.tokenizers = {}
        for feature in self.features:
            self.tokenizers[feature] = Tokenizer()

    def fillna(self, X):
        X.item_description = X.item_description.fillna("No description")
        X.name = X.name.fillna("No name")
        return X
    
    def fit(self, X, y=None):
        print('fitting_data')
        X = self.fillna(X)

        for feature in self.features:
            self.tokenizers[feature].fit_on_texts(X[feature].apply(str))
        
        print('data fitted')
        return self
    
    def transform(self, X, y=None):
        print('transforming data')
        item_condition = X.item_condition_id
        shipping = X.shipping
        output = [item_condition, shipping]
        X = self.fillna(X)

        for i, feature in enumerate(self.features):
            text_sequence = self.tokenizers[feature].texts_to_sequences(X[feature].apply(str))
            pad = pad_sequences(text_sequence, padding='post', maxlen=self.max_lengths[i])
            output.append(pad)
        
        print('data transformed')
        
        return output