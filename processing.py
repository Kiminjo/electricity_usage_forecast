import pandas as pd
from datetime import datetime

def date_time_split_1(data) :
    data['date'] = pd.to_datetime(data['date'])

    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['weekday'] = data['date'].dt.weekday
    data['hour'] = data['date'].dt.hour

    data = data.drop(['date'], axis = 1)

    return data


def date_time_split_2(data):
    time = data['dates']

    date_list = []
    year = []
    month = []
    day = []
    hour_list = []
    weekday = []

    for time_data in time:
        date = time_data.split(' ')[0]
        hour = time_data.split(' ')[1].split(':')[0]

        d = datetime.strptime(date, '%Y-%m-%d')
        date_list.append(pd.to_datetime(date))
        year.append(int(d.year))
        month.append(int(d.month))
        day.append(int(d.day))
        weekday.append(int(d.weekday()))

        if hour != '24':
            hour_list.append(int(hour))
        else:
            hour_list.append(int('00'))

    data = data.reset_index(drop=True)
    time_dataframe = pd.DataFrame({'year': year, 'month': month, 'day': day, 'weekday' : weekday, 'hour' : hour_list})
    dataframe = pd.concat([data, time_dataframe], axis=1, join='inner')
    dataframe = dataframe.drop(['dates'], axis = 1)

    return dataframe

def make_hourly_data(data) :
    
    datas = data.copy()

    for i in range(0, 24) :
        data = pd.concat([data, datas], axis = 0 , join = 'outer')
        data.sort_values(by = ['date'], inplace = True)
        data.reset_index(drop = True, inplace = True)

    return data

def fill_date(data) :
    period = pd.date_range(start = data.date.min(), end = data.date.max())
    time_data = pd.DataFrame({'period' : period})

    time_data = data_time_split_1(time_data)