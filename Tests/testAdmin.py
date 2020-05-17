import unittest
import Admin
from mock import patch

class test_admin(unittest.TestCase):

    # Returns True or False.
    def testConnectDatabase(self):
        with patch('Admin.sqlite3') as mock:
            mock.connect().cursor().fetchall().return_value = ['aims.db']
            assert(Admin.sqlConn())

    def testLogin(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.login())
            assert(X, "Success")

    def testCreateMp(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.createMp(Admin.con))
            assert(X, "Success")

    def testInsertMp(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.insertMp(Admin.con))
            assert(X, "Success")

    def testUpdateMp(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.updateMp(Admin.con))
            assert(X, "Success")

    def testDeleteMp(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.deleteMp(Admin.con))
            assert(X, "Success")

    def testCreateSt(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.createSt(Admin.con))
            assert(X, "Success")

    def testInsertSt(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.insertSt(Admin.con))
            assert(X, "Success")

    def testDeleteSt(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.deleteSt(Admin.con))
            assert(X, "Success")

    def testUpdateSt(self):
        with patch('Admin.sqlite3') as test:
            test.connect().cursor().fetchall().return_value = ['aims.db']
            X = bool(Admin.updateSt(Admin.con))
            assert(X, "Success")


if __name__ == '__main__':
    unittest.main()