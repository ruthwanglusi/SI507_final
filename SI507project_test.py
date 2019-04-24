import unittest
import sqlite3
from SI507project_tool_app import *

class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("park_info.db")
        self.cur = self.conn.cursor()

    #test for query the park table
    def test_park_query(self):
        res = self.cur.execute("select * from PARK")
        data = res.fetchall()
        self.assertTrue(data, 'testing that queries can be made to the park table')

    #test the database for fetching the id given a state name
    def test_state_table(self):
        self.cur.execute("select id from STATE where name = 'AL'")
        data = self.cur.fetchone()
        self.assertEqual(data, (1,))

    #test the database for fetching the id given a park type
    def test_type_table(self):
        self.cur.execute("select id from TYPE where name = 'National Monument'")
        data = self.cur.fetchone()
        self.assertEqual(data, (1,))

    #test for inserting a new park type
    def test_park_insert(self):
        park = ('Test Park', 'National Monument', 'AL')
        parkC = ('Test Park', 'National Monument', 'AL')
        self.cur.execute("insert into PARK(name, type_id, states) values (?,(select id from TYPE where name=?), (select id from STATE where name=?))", park)
        self.conn,commit()

        self.cur.execute("select type, states from PARK where name='Test Park'")
        data = self.cur.fetchone()
        self.assertEqual(data, parkC, 'testing select statement after inserting the park')

    def tearDown(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

# this test is written in reference to SI507_HW5_test.py provided by the instruction team
