import datetime
from pymongo import MongoClient
from mongoengine import *

connect('mongoengine_UmuziProspects', host='localhost', port=27017)
client = MongoClient("mongodb://root:pass@localhost:27017")

db = client["pymongo_UmuziProspects"]
my_db = db["Visitors"]

mylist = [
  { "visitor_name": "Scott", "visitors_age": 24, "date of visit": "2020-19-4", "time of visit": "9:00 am", "assistance_name": "Kevin", "comments": "He was very helpful and polite"},
  { "visitor_name": "Carry", "visitors_age": 28, "date of visit": "2020-21-8", "time of visit": "11:00 am", "assistance_name": "Lou", "comments": "He was very impatient"},
  {"visitor_name": "Viola", "visitors_age": 21, "date of visit": "2020-5-5", "time of visit": "13:00 pm", "assistance_name": "Sam", "comments": "She was kind"},
  
]

class Create_Visitor():
    x = my_db.insert_many(mylist)
    print(x.inserted_ids)
   

class list_Vistors():
    x = my_db.find_one()
    print(x)

class delete_Visitor():
    my_query = { "visitor_name": "Scott" }
    my_db.delete_one(my_query)

    #print the customers collection after the deletion:
    for x in my_db.find():
        print(x)

class delete_all():
    x = my_db.delete_many({})
    print(x.deleted_count, " documents deleted.")

class update_Visitor():
    my_query = { "visitor_name": "Scott"}
    new_values = { "$set": { "vistor_name": "Minne" } }

    my_db.update_one(my_query, new_values)

# print "Visitors" after the update:
    for x in my_db.find():
       print(x)

class list_all_details():
    for x in my_db.find():
       print(x)

print(db)

