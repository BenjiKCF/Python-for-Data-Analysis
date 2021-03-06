# Resampling, seconds > day
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken="zpFWg7jpwtBPmzA8sT2Z")
    df.columns = ['Value']
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('D').mean()
    df = df.resample('M').mean()
    df.columns = ['M30']
    return df

def state_list():
    fiddy_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
    return fiddy_states[0][1][2:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken="zpFWg7jpwtBPmzA8sT2Z")
        df.columns = [str(abbv)]
        # df = df.pct_change() # percentage of every year
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0 # cumulative percentage change # compound

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print main_df.head()

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken="zpFWg7jpwtBPmzA8sT2Z")
    df.columns = ['United_States']
    # df.rename(columns={'Value':'United_States'}, inplace=True)
    df["United_States"] = (df["United_States"] - df["United_States"][0]) / df["United_States"][0] * 100.0
    return df

m30 = mortgage_30y()
HPI_data = pd.read_pickle('fiddy_states.pickle')
HPI_bench = HPI_Benchmark()

state_HPI_M30 = HPI_data.join(m30)
print (state_HPI_M30.corr()['M30'].describe())
