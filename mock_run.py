import csv
import time
from os import path

from users import Users
import configuration as conf


def create_users_file():
    if path.exists(conf.USERS_FILE):
        return
    with open(conf.USERS_FILE, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow(conf.USERS_FILE_COL)


def mock_run():
    users = Users()
    users.import_users(conf.USERS_FILE)
    user = users.user_login("Shaked", "123456")
    if not user:
        user = users.add_new_user("Shaked", "123456")
        print("created user")
    running = user.create_activity("Sport", "Yoga")
    running.start_activity()
    time.sleep(5)
    running.end_activity()


def mock_run_new():
    create_users_file()
    users = Users()
    user = users.add_new_user("Shaked", "123456")
    running = user.create_activity("Sport", "Run")
    running.start_activity()
    time.sleep(5)
    running.pause_activity()
    time.sleep(10)
    running.resume_activity()
    time.sleep(10)
    running.end_activity()


if __name__ == "__main__":
    mock_run_new()
    print("@@")
    mock_run()
