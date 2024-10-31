from Hashing import hash_pwd

class Registration(object):

    def registerUser(self, userName, pwd):
        hashed_password = hash_pwd(pwd)

        with open("users.txt", "a") as file:
            file.write(f"{userName},{hashed_password}\n")

        print("Registration successful!")