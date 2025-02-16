#Post 
from datetime import datetime
#from user import User # ask professor 
class Post:
    # Class attribute to track total number of posts
    post_count = 0

    def __init__(self, author, content: str, tags: set = None):
        # Validate the content
        if  self.is_valid_content(content)==False:
            raise ValueError("Invalid post content.")
        
        # Set the protected instance attributes
        self._author = author
        self._content = content
        self._created_on = datetime.now()
        self._tags = set()  # Initialize empty set for tags
        self._liked_by = []  # List of users who liked the post
        self._comments = []  # List of comments on the post

        # Validate and set the tags if provided
        if tags is not None:
            for tag in tags:
                if self.is_valid_tag(tag)==False:
                    raise ValueError("Invalid tag.")
                self._tags.add(tag)

        # Increment the post count when a new post is created
        Post.post_count += 1

    # Getter for content (read-only)
    @property
    def content(self) -> str:
        return self._content

    # Getter for created_on (read-only)
    @property
    def created_on(self) -> datetime:
        return self._created_on

    # Getter for tags (read-only)
    @property
    def tags(self) -> set:
        return self._tags

    # Getter for liked_by (read-only)
    @property
    def liked_by(self) -> list:
        return self._liked_by

    # Method to add a tag to the post
    def add_tag(self, tag: str):
        if self.is_valid_tag(tag):
            self._tags.add(tag)
        else:
            raise ValueError("Invalid tag.")

    # Method to remove a tag from the post
    def remove_tag(self, tag: str):
        self._tags.discard(tag)  # discard does not raise an error if tag is not present

    # Static method to validate a tag
    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        return (tag.isalnum() and len(tag) <= 30)

    # Static method to validate the content
    @staticmethod
    def is_valid_content(content: str) -> bool:
        return (3 <= len(content) <= 2200)

    # Class method to return the total number of posts
    @classmethod
    def get_post_count(cls) -> int:
        return cls.post_count
