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

#print (housing_data.tail())

X = np.array(housing_data.drop(['label', 'US_HPI_future'], 1)) # 1 = column
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
