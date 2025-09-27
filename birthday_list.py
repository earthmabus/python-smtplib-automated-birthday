import pandas
import datetime as dt

BIRTHDAY_FILE = "./inputs/birthdays.csv"

class BirthdayList:
    def __init__(self):
        self.m_df_birthday_list = None
        pass

    def load(self):
        '''loads the list of birthdays'''
        self.m_df_birthday_list = pandas.read_csv(BIRTHDAY_FILE)

    def get_birthdays_for_date(self, month, day):
        '''returns a list of dict of people who matched birthdays on the specified month and day'''
        df_matches_month = self.m_df_birthday_list[self.m_df_birthday_list['month'].eq(month)]
        df_matches_month_and_day = df_matches_month[df_matches_month['day'].eq(day)]
        return df_matches_month_and_day.to_dict(orient='records')

