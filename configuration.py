
DATA_FILE = "{user_id}_data.csv"
COL_START = "start"
COL_END = "end"
COL_CATEGORY = "category"
COL_ACTIVITY = "activity"
COL_PAUSED = "paused"
COL_DURATION = "duration"
DATA_FILE_COL = [
    COL_START,
    COL_END,
    "s_year",
    "e_year",
    "s_month",
    "e_month",
    "s_day",
    "e_day",
    "s_hour",
    "e_hour",
    COL_CATEGORY,
    COL_ACTIVITY,
    COL_PAUSED,
    COL_DURATION,
]

USERS_FILE = "users.csv"
U_COL_ID = "id"
U_COL_NAME = "user_name"
U_COL_PASS = "password"
USERS_FILE_COL = [
    U_COL_ID,
    U_COL_NAME,
    U_COL_PASS,
]

# Error messages
E_ACTIVITY_EXISTS = "ERROR: Activity already exist"
E_CATEGORY_EXISTS = "ERROR: Category already exist"
E_ACTIVITY_DOESNT_EXISTS = "ERROR: Activity doesn't exist"
E_CATEGORY_DOESNT_EXISTS = "ERROR: Category doesn't exist"