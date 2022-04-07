import csv
import uuid
from user import User
import configuration as conf


class Users:
    def __init__(self, users_file=conf.USERS_FILE):
        self.ids_list = []
        self.users_list = []
        self.users_file = users_file

    def import_users(self, users_file, create_users=False):
        with open(users_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                id, name, password = row
                if create_users:
                    self.add_new_user(name, password)
                else:
                    self.__add_user(id, name, password)

    @staticmethod
    def generate_user_id():
        return uuid.uuid4()

    def __add_user(self, user_id, user_name, password):
        user = User(user_id, user_name, password)
        self.ids_list.append(user_id)
        self.users_list.append(user)
        return user

    def add_new_user(self, user_name, password):
        user_id = self.generate_user_id()
        user = self.__add_user(user_id, user_name, password)
        with open(self.users_file, 'a', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow([user_id, user_name, password])

        user.create_data_file()
        return user

    def users_exists(self, id):
        return id in self.ids_list

    def user_login(self, user_name, password):
        user = [u for u in self.users_list if u.user_name == user_name]
        if user:
            if user[0].password == password:
                return user[0]
        return False
