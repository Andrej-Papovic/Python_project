from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://admin:admin@cluster0.vjyox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["users_vouchers"]
mongo_collection = mongo_db["vouchers"]

print(mongo_collection)