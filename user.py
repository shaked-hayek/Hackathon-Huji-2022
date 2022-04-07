import uuid
import configuration as conf
import csv


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_id = self.generate_user_id()
        self.file_name = conf.DATA_FILE.format(self.user_id)
        self.create_data_file()

    @staticmethod
    def generate_user_id():
        return uuid.uuid4()

    def add_user(self):
        with open(conf.USERS_FILE, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([self.user_id, self.user_name, self.password])

    def create_data_file(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([conf.DATA_FILE_COL])
