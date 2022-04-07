import pandas as pd
import matplotlib.pyplot as plt


def change_from_user_avg(last_activity_dur, df_activity, period):
    df_period = df_activity.resample(period, on='start')['duration'].mean().dropna()
    return ((last_activity_dur - df_period.mean()) / df_period.mean()) * 100


class Insight:
    def __init__(self, userpath, all_users_path):
        self.df = pd.read_csv(userpath, parse_dates=['start', 'end']).dropna()
        self.activities = set(self.df['activity'].tolist())
        print(self.df.head())

    def end_activity_review(self):
        last_activity = self.df.iloc[-1]
        data = self.df[:-1]
        df_activity = self.df[self.df['activity'] == last_activity['activity']]
        print(change_from_user_avg(last_activity['duration'], data, 'D'))

    def period_overview(self):
        pass


if __name__ == '__main__':
    insight = Insight("123_data.csv", None)
    insight.end_activity_review()
