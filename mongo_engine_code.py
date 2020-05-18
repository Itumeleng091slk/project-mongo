import datetime
import pymongo
from pymongo import MongoClient
from mongoengine import *

connect('mongoengine_UmuziProspects', host='localhost', port=27017)
client = MongoClient("mongodb://root:pass@localhost:27017")

db = client["UmuziProspects"]
my_db = db["Visitors"]

mylist = [
  { "visitor_name": "Scott", "visitors_age": 24, "date of visit": "2020-19-4", "time of visit": "9:00 am", "assistance_name": "Kevin", "comments": "He was very helpful and polite"},
  { "visitor_name": "Carry", "visitors_age": 28, "date of visit": "2020-21-8", "time of visit": "11:00 am", "assistance_name": "Lou", "comments": "He was very impatient"},
  {"visitor_name": "Viola", "visitors_age": 21, "date of visit": "2020-5-5", "time of visit": "13:00 pm", "assistance_name": "Sam", "comments": "She was kind"},
  
]

class Visitor:

    def __init__(self):
        pass

    def Create_Visitor(self, *args):
        visitor = my_db.insert_many(mylist)
        return visitor.inserted_ids
    
    def list_Vistors(self, *args):
        visitor = my_db.find_one()
        return visitor

    def delete_Visitor(self, *args):
        my_query = { "visitor_name": "mylist" }
        my_db.delete_one(my_query)
        for visitor in my_db.find(): #print the customers collection after the deletion
            return visitor

    def delete_all(self, *args):
        visitor = my_db.delete_many({})
        return visitor.deleted_count, " documents deleted."

    def update_Visitor(self, *args):
        my_query = { "visitor_name": "mylist"}
        new_values = { "$set": { "vistor_name": "mylist" } }
        my_db.update_one(my_query, new_values)
        for visitor in my_db.find(): # print "Visitors" after the update
            return visitor

    def list_all_details(self, *args):
        for visitor in my_db.find():
            return visitor

visitor_1 = Visitor()
print(visitor_1.update_Visitor())


