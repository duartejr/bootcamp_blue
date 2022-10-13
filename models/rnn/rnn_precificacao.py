import pandas as pd
import numpy as np

from prep_data import *

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras import layers
from tensorflow.keras.models import Model

import tensorflow_addons as tfa
from sklearn import metrics

from sklearn.pipeline import Pipeline
import pickle

# Carrega o rnn
rnn = keras.models.load_model('rnn_keras.h5', compile=False)

# Carrega a pipeline
with open(f'pipeline.pickle', 'rb') as handle:
  pipeline = pickle.load(handle)

# Adiciona a rnn a nova pipeline
pipeline.steps[1] = ('model', rnn)