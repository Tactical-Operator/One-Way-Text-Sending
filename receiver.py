from pymongo import MongoClient
import time

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://ashwin_141:ashwin_chat_1234@cluster0.6flcgip.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["chat"]
collection = db["messages"]

print("Simple Receiver Started.")

while True:
    # Find one message that is not yet delivered
    msg = collection.find_one({"delivered": False})
    if msg:
        print("\nNew Message:", msg["message"])
        # Mark message as delivered
        collection.update_one(
            {"_id": msg["_id"]},
            {"$set": {"delivered": True}}
        )
    time.sleep(1)  # sleep for 1 second
