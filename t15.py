import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn import svm, preprocessing, cross_validation # preprocessing convert (-1 to 1) # cross_validation create test

style.use('fivethirtyeight')

# authtoken="zpFWg7jpwtBPmzA8sT2Z"

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:  # if rise
        return 1
    else:
        return 0

housing_data = pd.read_pickle('HPI.pickle')

housing_data = housing_data.pct_change()

# shift future value to current date
housing_data['US_HPI_future'] = housing_data['United_States'].shift(-1)
housing_data.replace([-np.inf, np.inf], np.nan, inplace=True)
housing_data.dropna(inplace=True)

housing_data['label'] = list(map(create_labels, housing_data['United_States'], housing_data['US_HPI_future']))

housing_data['ma_apply_example'] = housing_data['M30'].rolling(window=10).mean()

print (housing_data.tail())
