import pandas as pd
from datetime import timedelta

from .api import *


class DayAheadLoadForecast(API):
    def __init__(self, file_type='DayAheadLoadForecast', start_date=None, end_date=None):
        super(DayAheadLoadForecast, self).__init__(file_type, start_date, end_date)
        # self.file_type = 'DayAheadLoadForecast'
        # self.start_date = start_date
        # self.end_date = end_date

    def main(self):
        files = self.get_files()
        data = pd.DataFrame()
        for file in files:
            day = pd.to_datetime(file.split('/')[-1].split('_')[0])
            df = pd.read_excel(file, header=2)
            df.set_index(df.columns[0], inplace=True, drop=True)
            df = df.T
            df['Version'] = int(file.split('_')[-1].split('.')[0])
            df.index = pd.date_range(day, day+timedelta(hours=23), freq='1H')
            data = data.append(df)
        data.index.name = 'Date'
        data.sort_values(by=['Date', 'Version'], inplace=True)
        return data


if __name__ == '__main__':
    df = DayAheadLoadForecast(start_date='2020-10-01', end_date='2020-10-02').main()
    df.head()