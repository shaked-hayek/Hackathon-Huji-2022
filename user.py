import csv
from os import path
import configuration as conf
from activity import Activity


class User:
    def __init__(self, user_id, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_id = user_id

    def create_data_file(self):
        file_name = conf.DATA_FILE.format(user_id=self.user_id)
        if path.exists(file_name):
            return
        with open(file_name, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(conf.DATA_FILE_COL)

    def create_activity(self, category, name):
        return Activity(self.user_id, category, name)
