import unittest
from mongo_engine_code import Visitor

visitors = Visitor()

class Test_mongo(unittest.TestCase):

    def test_Create_Visitor(self):
        assert visitors.Create_Visitor
    
    def test_list_Vistors(self):
        assert visitors.list_Vistors

    def test_delete_Visitor(self):
        assert visitors.delete_Visitor

    def test_delete_all(self):
        assert visitors.delete_all

    def test_update_Visitor(self):
        assert visitors.update_Visitor

    def test_list_all_details(self):
        assert visitors.list_all_details


if __name__ == '__main__':
    unittest.main()
