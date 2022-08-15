from tkinter import *
from tkinter import ttk


class LoginApp:

    def __init__(self, root, users):

        self.users = users  # users stored in dictionary
        self.logged_in = False

        root.title("Login")
        root.geometry('300x300')

        # upper_window contains "Username" and "Password" text and their associated Entry fields, stacked vertically
        self.upper_window = ttk.Frame(root, padding='0.35i')

        # "Username" text and associated entry field
        self.username_label = Label(self.upper_window,
                                    text="Username",
                                    font=("Arial", 10, 'bold'))
        self.username_label.pack()
        self.login_field_username = Entry(self.upper_window,
                                          width=21,
                                          font=('Arial', 11))
        self.login_field_username.pack(pady=(4, 20))

        # "Password" text and associated entry field
        self.password_label = Label(self.upper_window,
                                    text="Password",
                                    font=("Arial", 10, 'bold'))
        self.password_label.pack()
        self.login_field_password = Entry(self.upper_window,
                                          width=21,
                                          font=('Arial', 11))
        self.login_field_password.pack(pady=4)
        self.upper_window.pack()

        # create lower frame to hold log in and sign up buttons, create buttons
        self.lower_window = ttk.Frame(root)
        self.login_button = Button(self.lower_window,
                                   command=self.sign_in,
                                   text="LOG IN",
                                   relief=RAISED,
                                   height=1,
                                   width=8,
                                   border=3,
                                   font=('Arial', 10, 'bold')).grid(column=1, row=0, padx=10)
        self.sign_up_button = Button(self.lower_window,
                                     command=self.sign_up,
                                     text="SIGN UP",
                                     relief=RAISED,
                                     height=1,
                                     width=8,
                                     border=3,
                                     font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=10)
        self.lower_window.pack()

    # returns True if username is found in the user database dictionary
    def check_users(self, username):
        username_list = [name for name in self.users.keys()]
        if username in username_list:
            return True
        else:
            return False

    # returns True if entered username and password match existing login credentials
    def check_password(self, username, password):
        if self.users[username] == password:
            return True
        else:
            return False

    # prompts user to fill login/sign up fields if either is left empty
    # attempts to log in if both fields are filled
    def sign_in(self):
        username = self.login_field_username.get()
        password = self.login_field_password.get()
        if username and password and self.check_users(username):
            if self.check_password(username, password):
                self.logged_in = True
                print("Logged in!")
            else:
                print("Incorrect password. Please try again.")
        elif username and password and not self.check_users(username):
            print("That user does not exist.")
        elif password and not username:
            print("Please enter your username.")
        elif username and not password:
            print("Please enter your password.")
        elif not username or password:
            print("Please enter your credentials.")

    # prompts user to fill sign up/login fields if either is left empty
    # creates user profile if username doesn't already exist in the user database
    def sign_up(self):
        username = self.login_field_username.get()
        password = self.login_field_password.get()
        if username and password and not self.check_users(username):
            print("Signed up!")
            self.users[username] = password
            print(self.users)
        elif self.check_users(username):
            print("That username is already in use.")
        elif password and not username:
            print("Please enter a username.")
        elif username and not password:
            print("Please enter a password.")
        elif not username or password:
            print("Please enter a username and password.")


user_database = {'tammy': 'password', 'greg': 'keebler', 'fard': 'pineapple'}

root = Tk()
LoginApp(root, user_database)
root.mainloop()
