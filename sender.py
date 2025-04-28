from pymongo import MongoClient

Mongo_URL="Tour MONGODB CLUSTER LINK "

client=MongoClient(Mongo_URL)
db=client["chat"]
collection=db["messages"]

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
