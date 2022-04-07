import configuration as conf
import csv
from datetime import datetime


class Activity:
    def __init__(self, user_id, activity_name):
        self.activity_name = activity_name
        self.user_id = user_id
        self.start_time = None
        self.end_time = None

    def start_activity(self):
        self.start_time = datetime.now()

    def finish_activity(self):
        self.end_time = datetime.now()

    def record_activity(self):
        duration = self.end_time - self.start_time
        with open(conf.DATA_FILE.format(self.user_id), 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([
                self.start_time.timestamp(),
                self.end_time.timestamp(),
                self.activity_name,
                duration.timestamp(),
            ])
