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
        self.paused_total = None
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

    def finish_activity(self):
        if self.start_time == None:
            print("ERROR: Activity not started yet")
            return
        self.end_time = datetime.now()

    def get_duration(self):
        total_duration = (self.end_time - self.start_time)
        return total_duration.seconds - self.paused_total

    def record_activity(self):
        with open(conf.DATA_FILE.format(self.user_id), 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([
                self.start_time.timestamp(),
                self.end_time.timestamp(),
                self.category,
                self.name,
                self.paused_total,
                self.get_duration(),
            ])
