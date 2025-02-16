# user.py
from datetime import datetime
import re

class User:
    # Class attribute to track total number of users
    user_count = 0

    def __init__(self, username: str, email: str):
        # Validate the username and email
        if  self.is_valid_username(username)==False:
            raise ValueError("Invalid username.")
        if  self.is_valid_email(email)== False :
            raise ValueError("Invalid email address.")

        # Set the protected instance attributes
        self._username = username
        self._email = email
        self._bio = ""  # Empty bio initially
        self._joined_on = datetime.now()  # Set the current date and time
        self._posts = []  # List of posts
        self._liked_posts = []  # List of liked posts
        self._comments = []  # List of comments
        self._liked_comments = []  # List of liked comments

        # Public instance attributes for social connections
        self.following = []  # List of followed users
        self.followers = []  # List of followers

        # Increment the user count when a new user is created
        User.user_count += 1

    # Getter for username (read-only)
    @property
    def username(self) -> str:
        return self._username

    # Getter for email (read-only)
    @property
    def email(self) -> str:
        return self._email

    # Getter for bio
    @property
    def bio(self) -> str:
        return self._bio

    # Setter for bio with validation
    @bio.setter
    def bio(self, new_bio: str)-> None:
        if len(new_bio) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = new_bio

    # Getter for joined_on (read-only)
    @property
    def joined_on(self) -> datetime:
        return self._joined_on

    # Getter for posts (read-only)
    @property
    def posts(self) -> list:
        return self._posts

    # Static method to validate the username
    @staticmethod
    def is_valid_username(username: str) -> bool:
        if len(username) < 3 or len(username) > 30:
            return False
        # Check if the username contains only alphanumeric characters, periods, or underscores
        for char in username:
            if not (char.isalnum() or char in ['.', '_']):
                return False
        return True

    # Static method to validate the email using a regular expression
    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    # Class method to return the current user count
    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count



