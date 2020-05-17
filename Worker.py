from Admin import con
#from Credentials import credentials

class Worker:

    def functions(self):

        options = {
            "1": ("File Complaint", self.fileComplaint)
        }

        ans = input("Choose:\n"
                        "1.File Complaint.\n")

        options.get(ans)[1](con)

    def login(self):
        mem_password = 3333

        enteredPassword = int(input("Enter password"))
        if enteredPassword == mem_password:
            self.functions()
        else:
            print("Try again")

    # def fileComplaint(self, con):
    #     cursor = con.cursor()
    #     cursor.execute('Create table if not exists File_Complaint (mid integer, Problem_Occured text, Status text)')
    #     con.commit()

    def fileComplaint(self, con):
        cur = con.cursor()
        mid = int(input("Enter mid:\n"))
        problem = str(input("Problem Occured:\n"))
        status = str(input("Status:\n"))
        cur.execute('Insert into File_Complaint (mid, Problem_Occured, Status) values (?, ?, ?)',(mid, problem, status ))
        con.commit()

mem = Worker()
mem.login()

