import unittest
import sqlite3
from SI507project_tool_database import *

class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("park_info.db")
        self.cur = self.conn.cursor()

    #test the database for fetching the state_id given a state name
    def test_state_table(self):
        self.cur.execute("select state_id where stateName = 'AL'")
        data = self.cur.fetchone()
        self.assertEqual(data, ('1', 'AL'))

    #test the database for fetching the type_id given a park type
    def test_state_table(self):
        self.cur.execute("select state_id where typeName = 'National Monument'")
        data = self.cur.fetchone()
        self.assertEqual(data, ('1', 'National Monument'))

    #test the database for inserting a new park
    def test_park_insert(self):
        park = ('Birmingham Civil Rights', 'National Monument', 'AL')
        parkC = ('Birmingham Civil Rights', 'National Monument', 'AL')
        self.cur.execute("insert into PARK(name, type, states) values (?,(select id from TYPE where typeName=?), (select id from STATE where typeName=?))",park)
        self.conn,commit()

        self.cur.execute("select type, states from PARK where name='Birmingham Civil Rights'")
        data = self.cur.fetchone()
        self.assertEqual(data, parkC, 'testing select statement after inserting the park')

    #test for query the park table
    def test_park_query(self):
        res = self.cur.execute("select * from PARK")
        data = res.fetchall()
        self.assertTrue(data, 'testing that queries can be made to the park table')

    #test for inserting a new park type
    def test_type_insert(self):
        type = ('National Military Park')
        self.cur.execute("insert into TYPE(typeName) values (?)", type)
        self.conn.commit()

        self.cur.execute("select id from TYPE where typeName = 'National Military Park'")
        data = self.cur.fetchone()
        self.assertEqual(data, type, 'testing select an id based on a type name')

    def tearDown(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)

# this test is written in reference to SI507_HW5_test.py provided by the instruction team
