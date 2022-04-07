import csv
from os import path
import configuration as conf
from activity import Activity


class User:
    def __init__(self, user_id, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_id = user_id
        self.activity_by_category = {}

    def create_data_file(self):
        file_name = conf.DATA_FILE.format(user_id=self.user_id)
        if path.exists(file_name):
            return
        with open(file_name, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(conf.DATA_FILE_COL)

    def create_activity(self, category, name):
        if category not in self.activity_by_category:
            print(conf.E_CATEGORY_DOESNT_EXISTS)
            return
        if name in self.activity_by_category[category]:
            print(conf.E_ACTIVITY_EXISTS)
            return
        self.activity_by_category[category].append(name)
        return Activity(self.user_id, category, name)

    def create_category(self, name):
        if name in self.activity_by_category:
            print(conf.E_CATEGORY_EXISTS)
            return
        self.activity_by_category[name] = []

    def delete_activity(self, category, name):
        if category not in self.activity_by_category:
            print(conf.E_CATEGORY_DOESNT_EXISTS)
            return False
        if name not in self.activity_by_category[category]:
            print(conf.E_ACTIVITY_DOESNT_EXISTS)
            return False
        self.activity_by_category[category].remove(name)
        return True

    def delete_category(self, name):
        if name not in self.activity_by_category:
            print(conf.E_CATEGORY_DOESNT_EXISTS)
            return False
        self.activity_by_category.pop(name)
        return True
