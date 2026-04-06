from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://hatamimohamad254_db_user:ImZghwL5Y9uCF0s2@cluster0.wg4025n.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database("hatamimohamad254_db")
# transaksi = db.get_collection("transaksi")

def get_db_connection():
    return db