from Login import login
from Admin import con

class Start:

    def main(self):
        """
        This is the main page for Aims console application.
        :return: True/False
        """
        option = {
            "1": ("admin login", login.check_admin),
            "2": ("supervisor team login", login.check_team),
            "3": ("employee login", login.check_emp)
        }

        ans = input("Choose:\n"
                    "1.Admin Login.\n"
                    "2.Supervising Team Login.\n"
                    "3.Employee Login.")

        option.get(ans)[1](con)

if __name__ == '__main__':
    Start().main()
