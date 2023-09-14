import hashlib

# Function to hash a password
def hash_password(password):
    salt = "random_salt"  # You should generate a random salt for each user in a real application
    password = password + salt
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to create a new account
def create_account(username, password):
    with open("save.txt", "a") as file:
        hashed_password = hash_password(password)
        file.write(f"{username}:{hashed_password}\n")
        print("Account created successfully!")

# Function to check login credentials
def login(username, password):
    with open("save.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_hashed_password = line.strip().split(":")
            if username == stored_username and hash_password(password) == stored_hashed_password:
                return True
        return False

# Main program
while True:
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        create_account(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            print("Login successful!")
        else:
            print("Login failed. Invalid credentials.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
