class Config(object):
    LOGGER = True
    API_ID = 21297196
    API_HASH = "f1b08c2946b1a5ff3c3c22e4c31b2f3b"
    TOKEN = "7997497208:AAGosiS2uVsZuqE83-2z9mDwThhKSVrrWu0"  
    OWNER_ID=6183284715
    
    SUPPORT_CHAT = "" 
    START_IMG = ""
    EVENT_LOGS = ()
    MONGO_DB_URI= "mongodb+srv://Sinchu:Sinchu@sinchu.qwijj.mongodb.net/?retryWrites=true&w=majority&appName=Sinchu"
   
    DATABASE_URL = "mongodb+srv://Sinchu:Sinchu@sinchu.qwijj.mongodb.net/?retryWrites=true&w=majority&appName=Sinchu"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 20
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
