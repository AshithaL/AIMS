import unittest
from Admin import con
from mock import patch
from Supervisior import Supervisor

class MyTestCase(unittest.TestCase):

    sup = Supervisor()

    def testLogin(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Supervisor.login)
            assert(X, "Success")
            assert(X, "Failure")

    def testShowreport(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Supervisor.showReport(self.sup, con))
            assert(X, "Success")
            assert(X, "Failure")

    def testSubmitToAdmin(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Supervisor.submit_to_admin(self.sup, con))
            assert(X, "Success")
            assert(X, "Failure")


if __name__ == '__main__':
    unittest.main()