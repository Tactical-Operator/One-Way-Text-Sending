from pymongo import MongoClient

Mongo_URL="mongodb+srv://ashwin_141:ashwin_chat_1234@cluster0.6flcgip.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

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