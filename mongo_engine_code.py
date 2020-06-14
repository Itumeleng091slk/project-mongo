import datetime
import pymongo
from visitors_data import mylist
from pymongo import MongoClient
from mongoengine import *
from credentials import *

connect('mongoengine_UmuziProspects', host='host', port=port)
client = MongoClient("mongodb://root:pass@host:port")

db = client["UmuziProspects"]
my_db = db["Visitors"]


class Visitor():
    
    def __init__(self, visitor_data):
        self.visitor_data = visitor_data

    def create_visitor(self):
        try:
            create_visitor = my_db.insert_many(self.visitor_data)
        except TypeError: 
            return "visitor not created"
        return "visitor created" 
         
    def delete_visitor(self,person_to_delete):
        try:
            delete_visitor = my_db.delete_one(person_to_delete)
        except AssertionError:
            return "visitor not deleted"
        return "visitor deleted"

    def update_visitor(self, visitor_to_update, new_info):
        try:
            update_visitor = my_db.update_one(visitor_to_update, new_info)
        except TypeError:
            return "visitor updated"
        return "visitor not updated"

    def list_all_details(self):
        return my_db.find()


# visitor_2 = Visitor(mylist)
# print(visitor_2.create_visitor())

# visitor_3 = Visitor(mylist)
# print(visitor_3.delete_visitor({"visitor_name": "Viola"}))

# visitor_4 = Visitor(mylist)
# print(visitor_4.delete_all())

# visitor_1 = Visitor(mylist)
# print(visitor_1.update_Visitor({"visitor_name": "Scott"}, {"$set": {"gender":"male"}}))

# visitor_5 = Visitor(mylist)
# print(visitor_5.list_all_details())


