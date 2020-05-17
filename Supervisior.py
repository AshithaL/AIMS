from Admin import con
#from Credentials import credentials

from pprint import pprint

class Supervisor:

    def functions(self):

        option = {
            "1": ("Show Report", self.showReport),
            "2": ("Submit to Admin", self.submit_to_admin)
        }

        ans = input("Choose:\n"
                        "1.Show Report.\n"
                        "2.Submit to Admin.\n")

        option.get(ans)[1](con)

    def login(self):
        gpm_password = 2222

        enteredPassword = int(input("Enter password"))
        if enteredPassword == gpm_password:
            self.functions()
        else:
            print("Try again")

    def showReport(self, con):
        cursor = con.cursor()
        cursor.execute("Select * from FileComplaint")
        con.commit()

    def submit_to_admin(self, con):
        cursor = con.cursor()
        po = str(input("Problem Occured-\n"))
        cause = str(input("Cause-\n"))
        eye_wit = str(input("Eye Witness-\n"))
        deaths = int(input("Deaths"))
        cursor.execute('Insert into To_Admin (Problem_Occured, Cause, Eye_Witness, Deaths_if_any) values (?, ?, ?, ?)', (po, cause, eye_wit, deaths))
        con.commit()

gpm = Supervisor()
gpm.login()