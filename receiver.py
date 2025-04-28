from pymongo import MongoClient
import time

# Replace with your MongoDB URI
MONGO_URI = ""

client = MongoClient(MONGO_URI)
db = client["chat"]
collection = db["messages"]

print("\033[38;2;57;255;20m" + r'''
    ____                 _                    ______          __  _            
   / __ \___  ________  (_)   _____  _____   /_  __/__  _____/ /_(_)___  ____ _
  / /_/ / _ \/ ___/ _ \/ / | / / _ \/ ___/    / / / _ \/ ___/ __/ / __ \/ __ `/
 / _, _/  __/ /__/  __/ /| |/ /  __/ /       / / /  __(__  ) /_/ / / / / /_/ / 
/_/ |_|\___/\___/\___/_/ |___/\___/_/       /_/  \___/____/\__/_/_/ /_/\__, /  
                                                                      /____/ 
                                                            By @Ashwin Jadhav
''' + "\033[0m")

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
