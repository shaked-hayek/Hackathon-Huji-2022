import configuration as conf
import csv


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_id = self.generate_user_id()
        self.file_name = conf.DATA_FILE.format(self.user_id)
        self.create_data_file()

    def generate_user_id(self):
        return 1

    def create_data_file(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([conf.DATA_FILE_COL])
