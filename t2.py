import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_Rate':[65,75,62,64,54,66]}

df = pd.DataFrame(web_stats)
#df.set_index('Day', inplace=True)
#print df.head()

#df2 = df.set_index('Day')
#print df2.head()

#print df['Visitors']
#print '\n '
#print df.Visitors
#print '\n '
#print df[['Bounce_Rate','Visitors']]
#def save_file():
#    df2.to_csv('t2.csv')
#    print "File saved"

#save_file()

#print df.Visitors.tolist()
#print np.array(df[['Bounce_Rate','Visitors']]) # list of two columns

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print df2
