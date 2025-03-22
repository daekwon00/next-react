# User class and mock database

class User:
    """
    User class representing a user in the system.
    """
    def __init__(self, id, name, email, bio):
        """
        Initialize a new User instance.

        Args:
            id (int): Unique identifier for the user.
            name (str): Name of the user.
            email (str): Email address of the user.
            bio (str): Bio of the user.
        """
        self.id = id
        self.name = name
        self.email = email
        self.bio = bio

    def update(self, data):
        """
        Update user attributes with the provided data.

        Args:
            data (dict): Dictionary containing attributes to update.
        """
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
            
        for key, value in data.items():
            if key != 'id' and hasattr(self, key):  # Don't allow changing the ID
                setattr(self, key, value)
                
    def to_dict(self):
        """
        Convert User instance to dictionary.

        Returns:
            dict: Dictionary representation of the user.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'bio': self.bio
        }

# Mock database to store users
users_db = {}

# CRUD Functions

def create_user(id, name, email, bio):
    """
    Creates a new user and adds it to the mock database.

    Args:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
        bio (str): Bio of the user.

    Returns:
        User: The created User instance.

    Raises:
        ValueError: If a user with the given ID already exists.
    """
    if id in users_db:
        raise ValueError(f"User with ID {id} already exists.")

    user = User(id, name, email, bio)
    users_db[id] = user
    return user

def get_user_by_id(user_id):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User or None: The User instance if found, else None.
    """
    return users_db.get(user_id)

def update_user(user_id, data):
    """
    Updates an existing user's details.

    Args:
        user_id (int): The ID of the user to update.
        data (dict): A dictionary containing the fields to update.

    Returns:
        User: The updated User instance.

    Raises:
        ValueError: If the user does not exist.
    """
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")

    user.update(data)
    return user

def list_users():
    """
    Lists all users in the mock database.

    Returns:
        list: A list of User instances.
    """
    return list(users_db.values())

# Utility Functions

def seed_mock_db():
    """
    Seeds the mock database with initial users.
    """
    create_user(0, "Alice Smith", "alice@example.com", "Software Developer from NY.")
    create_user(1, "Bob Johnson", "bob@example.com", "Graphic Designer from CA.")
    create_user(2, "Charlie Lee", "charlie@example.com", "Data Scientist from TX.") 