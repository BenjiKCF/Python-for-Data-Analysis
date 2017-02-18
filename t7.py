import quandl
import pandas as pd
import pickle

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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print main_df.head()
    # create a pickle
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

#grab_initial_state_data()
# load a pickle
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print HPI_data
# pandas can create a pickle within a few lines
# HPI_data.to_pickle('HPI_data.pickle')
# HPI_data2 = pd.read_pickle('HPI_data.pickle')
# print(HPI_data2)
