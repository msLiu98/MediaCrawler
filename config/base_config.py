# Desc: base config
PLATFORM = "xhs"
KEYWORDS = "健身,旅游"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookies
COOKIES = "web_session=xxxxcfed1566xxxxxxxxxxxxxxxxxxx;" # if platform is xhs, pleas set only web_session cookie attr

# redis config
REDIS_DB_HOST = "redis://127.0.0.1"  # your redis host
REDIS_DB_PWD = "123456"  # your redis password

# enable ip proxy
ENABLE_IP_PROXY = False

# retry_interval
RETRY_INTERVAL = 60 * 30  # 30 minutes

# playwright headless
HEADLESS = True

# save login state
SAVE_LOGIN_STATE = False

# save user data dir
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# max page num
MAX_PAGE_NUM = 20

# max concurrency num
MAX_CONCURRENCY_NUM = 10
