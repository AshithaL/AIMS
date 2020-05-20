import uuid
# import AIMS.Repository as repo
from sqlite3 import Error
import datetime
from Admin import con
import Admin


class employee:
    """
    This is Employee Class
    """
    def __init__(self, role_id):
        """
        Initializer method
        :param role_id:
        """
        self.role_id = role_id

    def selection(self):
        """
        Selection of features for Employee
        :return: True/False
        """
        option = {
            "1": ("File Complaint", self.file_complaint),
            "2": ("Show Complaint", self.show_complaint)
        }

        ans = input("Choose:\n"
                    "1.File Complaint.\n"
                    "2.Show Complaint.\n")

        option.get(ans)[1](con)

    def file_complaint(self):
        """
        Complain a file against any incident happened
        :return: True/False
        """
        try:
            print("file your complain here")
            created_at = datetime.datetime.today()
            complain_id = str(uuid.uuid4())
            description = input("Enter all the details about incident please: ")
            working_zone = input("Enter working zone where incident happened: ")
            if description and working_zone:
                accident_list = ["fire breakout", "gas leakage", "infrastructure damages", "other"]
                complain_type = None
                print("Choose complain type \n 1.Fire Breakout 2.Gas Leakage 3.Infrastructure Damages 4.Other")
                ch = (input("Write your complain type: ")).lower()
                while not ch in accident_list:
                    print("Entered complain type doesnt exist")
                    ch = (input("Write your complain type: ")).lower()
                connection = Admin.sqlConn()
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT into complains(complain_id,description,working_zone,role_id,status,created_at,"
                    "delete_value,verdict,complain_type) Values(\'{}\',\'{}\', "
                    "\'{}\', \'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(complain_id, description, working_zone,
                                                                                self.role_id,
                                                                                "open", created_at, "False", 'False',
                                                                                complain_type))
                connection.commit()
                cursor.close()
                print("Your complain is filed")
                return True
            print("Description or working zone is empty..Try again")
            return False
        except Error as e:
            print(e)
            return False

    def show_complaint(self):
        """
        Show list of complain filed
        :return: True/False
        """
        try:
            connection = Admin.sqlConn()
            cursor = connection.cursor()
            records = cursor.execute(
                "select complain_id,description,working_zone,status,created_at from complains where delete_value = "
                "\'False\' and role_id = \'{}\'".format(self.role_id)).fetchall()
            if records:
                print("All complains")
                for row in records:
                    print("Complain_id= ", row[0])
                    print("Description= ", row[1])
                    print("Working_zone= ", row[2])
                    print("Status= ", row[3])
                    print("Date of incident= ", row[4])
                    print("-----------------------")
                return True
            print("No complains found")
            return True
        except Error as e:
            print(e)
            return False
