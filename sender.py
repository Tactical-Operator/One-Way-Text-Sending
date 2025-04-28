from pymongo import MongoClient

Mongo_URL=""

client=MongoClient(Mongo_URL)
db=client["chat"]
collection=db["messages"]

print("\033[38;2;57;255;20m" + r'''
   _____                __             ______          __  _            
  / ___/___  ____  ____/ /__  _____   /_  __/__  _____/ /_(_)___  ____ _
  \__ \/ _ \/ __ \/ __  / _ \/ ___/    / / / _ \/ ___/ __/ / __ \/ __ `/
 ___/ /  __/ / / / /_/ /  __/ /       / / /  __(__  ) /_/ / / / / /_/ / 
/____/\___/_/ /_/\__,_/\___/_/       /_/  \___/____/\__/_/_/ /_/\__, /  
                                                               /____/  
                                                     By @Ashwin Jadhav
''' + "\033[0m")


print("Go ahead Type it out or just exit")

while True:
    message=input("~# ")
    if message.lower()=="exit":
        print("Closing Sender Program")
        break
    if message=="":
        continue
    collection.insert_one({
        "message":message,
        "delivered":False
    })

    print("Sent......")

client.close()
