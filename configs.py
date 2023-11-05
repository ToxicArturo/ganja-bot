# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "7615554"))
    API_HASH = getenv("API_HASH", "9636ba88d645d36a3a89cd9365af0caa")
    BOT_TOKEN = getenv("BOT_TOKEN", "6969258227:AAFDCdPU7RQhnlvGEuQu3jH3H2VP4Bfq2-w")
    FSUB = getenv("FSUB", "toxic_tv_24")
    CHID = int(getenv("CHID", "-1001831951100"))
    SUDO = list(map(int, getenv("SUDO", "1358626459").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Arturo:Arturo_pro@cluster0.zvn1iwr.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
