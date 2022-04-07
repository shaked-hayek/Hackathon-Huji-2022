import configuration as conf
import csv
from datetime import datetime


class Activity:
    def __init__(self, user_id, category, name):
        self.category = category
        self.name = name
        self.user_id = user_id
        self.start_time = None
        self.end_time = None
        self.paused_total = 0
        self.paused_start = None

    def start_activity(self):
        self.start_time = datetime.now()

    def pause_activity(self):
        if self.paused_start != None:
            print("ERROR: Activity not paused")
            return
        self.paused_start = datetime.now()

    def resume_activity(self):
        paused = datetime.now() - self.paused_start
        self.paused_start = None
        self.paused_total += paused.seconds

    def get_duration(self):
        total_duration = (self.end_time - self.start_time)
        return total_duration.seconds - self.paused_total

    def record_activity(self):
        with open(conf.DATA_FILE.format(user_id=self.user_id), 'a', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([
                self.start_time.timestamp(),
                self.end_time.timestamp(),
                self.start_time.year,   # s_year
                self.end_time.year,     # e_year
                self.start_time.month,  # s_month
                self.end_time.month,    # e_month
                self.start_time.day,    # s_day
                self.end_time.day,      # e_day
                datetime.strftime(self.start_time, "%H:%M:%S"),  # s_hour
                datetime.strftime(self.end_time, "%H:%M:%S"),    # e_hour
                self.category,
                self.name,
                self.paused_total,
                self.get_duration(),
            ])

    def end_activity(self):
        if self.start_time == None:
            print("ERROR: Activity not started yet")
            return
        self.end_time = datetime.now()
        self.record_activity()