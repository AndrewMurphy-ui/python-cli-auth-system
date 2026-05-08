from storage import save_cli



def is_valid_username(name, users):
    if not name:
        print("Error: username cannot be empty.")
        return False
    if name in users:
        print("Username already taken.")
        return False
    return True

def is_valid_password(password):
    if not password:
        print("Error: password cannot be empty.")
        return False
    return True

def register_user(users):
    """Register a new user by prompting for a unique username and password."""
    while True:
        name = input("Enter a username: ").lower().strip()
        if not is_valid_username(name, users):
            continue

        password = input("Enter a password: ").strip()
        if not is_valid_password(password):
            continue

        users[name] = password
        save_cli(users)

        print("you have signed up! Thank you!")






def login_name_validation(name, storage):
    """Validate a username"""
    if not name:
        print("Error: username cannot be empty.")
        return False

    if not name in storage:
        print("Error: username does not exist, try again!")
        return False
    return True


def password_validation(password):
    """Validate a password"""
    if not password:
        print("Error: password cannot be blank, try again!")
        return False
    return True






def login_user(name, password, users):
    """login a user"""
    while True:
        name = input("login name: ")
        if not login_name_validation(name, users):
            continue

        password = input("login password: ")
        if not password_validation(password):
            continue

        users[name] = password
        if name in users:
            if password == users[name]:
                print("success, you have logged in successfully!")
                return





