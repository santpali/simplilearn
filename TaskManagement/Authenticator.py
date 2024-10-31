from Hashing import hash_pwd
class Authenticator(object):

    # Function to login a user
    def login(self, userName, pwd):
        hashed_password = hash_pwd(pwd)

        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if u == userName and p == hashed_password:
                print("Login successful!")
                return userName

        print("Invalid username or password.")
        return None

