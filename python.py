import os
import sqlite3
import requests

# 🚨 Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(user, pwd):
    # 🚨 Insecure authentication (plaintext password comparison)
    if user == USERNAME and pwd == PASSWORD:
        return True
    return False

def run_system_command():
    # 🚨 Command injection vulnerability
    cmd = input("Enter a system command: ")  # No input sanitization
    os.system(cmd)  # Dangerous execution

def get_user_data():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🚨 SQL Injection vulnerability
    user_id = input("Enter user ID: ")  # No sanitization
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)  # Vulnerable to SQL injection

    print(cursor.fetchall())
    conn.close()

def download_file():
    url = input("Enter URL to download: ")  # 🚨 No validation of user input
    response = requests.get(url)  # 🚨 No SSL verification
    print(response.text)

def main():
    print("1. Authenticate")
    print("2. Run System Command")
    print("3. Get User Data")
    print("4. Download File")

    choice = input("Choose an option: ")

    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")
        if authenticate(user, pwd):
            print("Authenticated successfully!")
        else:
            print("Authentication failed!")

    elif choice == "2":
        run_system_command()

    elif choice == "3":
        get_user_data()

    elif choice == "4":
        download_file()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
