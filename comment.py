# comment.py

from datetime import datetime
# ask professor on Optional
class Comment:
    # Class attribute to track total number of comments
    comment_count = 0

    def __init__(self, author, content, tags=None):
        # Validate the content
        if  self.is_valid_content(content)==False:
            raise ValueError("Invalid comment content.")
        
        # Set the protected instance attributes
        self._author = author
        self._content = content
        self._created_on = datetime.now()
        self._tags = set()  # Initialize empty set for tags
        self._liked_by = []  # List of users who liked the comment

        # Validate and set the tags if provided
        if tags:
            for tag in tags:
                if  self.is_valid_tag(tag)==False:
                    raise ValueError("Invalid tag")
                self._tags.add(tag)

        # Increment the comment count when a new comment is created
        Comment.comment_count += 1

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

    # Method to add a tag to the comment
    def add_tag(self, tag: str):
        if self.is_valid_tag(tag):
            self._tags.add(tag)
        else:
            raise ValueError("Invalid tag.")

    # Method to remove a tag from the comment
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

    # Class method to return the total number of comments
    @classmethod
    def get_comment_count(cls) -> int:
        return cls.comment_count
