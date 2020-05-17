import unittest
from Admin import con
from mock import patch
from Worker import Worker

class MyTestCase(unittest.TestCase):

    member = Worker()

    def testLogin(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Worker.login(self.member))
            assert(X, "Success")

    def testfileComplaint(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Worker.fileComplaint(self.member, con))
            assert(X, "Success")


if __name__ == '__main__':
    unittest.main()