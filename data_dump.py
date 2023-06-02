
import pymongo
import pandas as pd
import json




from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Anamay1:Anamay123@cluster0.rwbawcb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

Data_file_path = r"D:\\projects\\DSproject\\DSProject\\insurance.csv"

database_name = "INSURANCE"
collection_name = "INSURANCE_PROJECT"


if __name__ == "__main__":
    df = pd.read_csv(Data_file_path)
    print(f"Rows and columns:{df.shape}")
    df.reset_index(drop = True, inplace =True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[database_name][collection_name].insert_many(json_record)

     