class User:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.users[username] = {"password": password, "ratings": {}}
        print("Registration successful!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_data = self.users.get(username)
        if user_data and user_data["password"] == password:
            self.current_user = username
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def rate_movie(self, movie_id, rating):
        user_data = self.users.get(self.current_user)
        if user_data:
            user_data["ratings"][movie_id] = rating
            print("Movie rating added.")
        else:
            print("User not found.")

    def get_user_id(self):
        return self.current_user
