import unittest
from visitors_data import mylist
from mongo_engine_code import Visitor

class Test_mongo(unittest.TestCase):   

    def test_create_visitor(self):
        visitors = Visitor(mylist)
        assert visitors.create_visitor() == "visitor created"
    
    def test_visitor_not_created(self):
        visitors = Visitor("this is a string")
        assert visitors.create_visitor() == 'visitor not created'

    def test_delete_Visitor(self):
        visitors = Visitor(mylist)
        assert visitors.delete_visitor("Viola") == "visitor delete

    def visitor_updated(self):
        visitors = Visitor("this is a string")
        assert visitors.update_visitor("Scott", "male") == "visitor updated"

    def test_visitor_not_updated(self):
        visitors = Visitor(mylist)
        assert visitors.update_visitor("Scott", "male") != "visitor not updated"

    def test_list_all_details(self):
        visitors = Visitor(mylist)
        assert visitors.list_all_details()

if __name__ == '__main__':
    unittest.main()

