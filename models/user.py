# User model
class User:
    def __init__(self, username, phone_number):
        self.username = username
        self.phone_number = phone_number
        
    def __repr__(self):
        return f"User(username={self.username}, phone_number={self.phone_number})"