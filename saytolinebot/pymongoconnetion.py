import pymongo

def connect_to_mongodb():
    try:
        connection_url = "mongodb+srv://yexuanncu:110524031@useragentlog.zgtv7zp.mongodb.net/"
        client = pymongo.MongoClient(connection_url)
        print("Success connect to MongoDB！")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print("Fail to connect MongoDB！:", e)
        return None