#import quandl
import pandas as pd

#df = quandl.get("FMAC/HPI_AK", authtoken="zpFWg7jpwtBPmzA8sT2Z", start_date="1999-01-31")

#print df.head()

fiddy_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')

# first DataFrame, # second columns # start from 2th row
for abbv in fiddy_states[0][1][2:]:
    print ("FMAC/HPI_{}".format(abbv))
