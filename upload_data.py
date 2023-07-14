import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://hellokunal:Wafer@cluster0.hrdp8gn.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# create database name and collection name
DATABASE_NAME="waferfault_detection_database"
COLLECTION_NAME="waferfault_data"

# read the data as a dataframe
df=pd.read_csv(r"F:\machine_learning_projects\wafer-fault-detection-2\notebooks\wafer.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)