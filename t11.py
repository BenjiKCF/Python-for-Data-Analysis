# Resampling, seconds > day
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

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

# grab_initial_state_data()

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken="zpFWg7jpwtBPmzA8sT2Z")
    df.columns = ['United_States']
    # df.rename(columns={'Value':'United_States'}, inplace=True)
    df["United_States"] = (df["United_States"] - df["United_States"][0]) / df["United_States"][0] * 100.0
    return df

# Graph of HPI USA and all states
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0)) # 2,1, 1graph on top, 1at bottom
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

HPI_data = pd.read_pickle('fiddy_states.pickle')
TX_AK_12corr = HPI_data['TX'].rolling(window=12).corr(HPI_data['AK'])

HPI_data['TX'].plot(ax=ax1, label='TX HPI')
HPI_data['AK'].plot(ax=ax1, label='TX HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

#HPI_data['TX12MA'] = HPI_data['TX'].rolling(window=12, center=False).mean()
#HPI_data['TX12STD'] = HPI_data['TX'].rolling(window=12, center=False).std()

#print HPI_data[['TX', 'TX12MA', 'TX12STD']].head()

#HPI_data[['TX', 'TX12MA']].plot(ax = ax1)
#HPI_data[['TX12STD']].plot(ax = ax2)
plt.show()
