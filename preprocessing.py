import pandas as pd
import statistics

def make_sum_column (data) :

    data['NX_total'] = [0] * len(data)

    for length in range(len(data)) :
        data['NX_total'][length] = data.iloc[length, 1 : -1].sum()

    return data

def time_data (data) :

    data['Time'] = pd.to_datetime(data['Time'])

    data['day'] = data['Time'].dt.day
    data['month'] = data['Time'].dt.month
    data['year'] = data['Time'].dt.year
    data['hour'] = data['Time'].dt.hour

    return data