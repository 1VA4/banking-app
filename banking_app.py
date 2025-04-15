import mysql.connector

# Function to check account balance
def check_balance(user_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
    balance = cursor.fetchone()
    connection.close()
    
    if balance:
        return balance[0]  # Return the balance
    else:
        return "Account not found"


# Function to deposit funds into an account
def deposit(user_id, amount):
    if amount <= 0:
        return "Deposit amount must be positive"
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE user_id = %s", (amount, user_id))
    connection.commit()
    connection.close()
    
    return "Deposit successful"


# Function to withdraw funds from an account
def withdraw(user_id, amount):
    if amount <= 0:
        return "Withdrawal amount must be positive"
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
    balance = cursor.fetchone()
    
    if balance and balance[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE user_id = %s", (amount, user_id))
        connection.commit()
        connection.close()
        return "Withdrawal successful"
    else:
        connection.close()
        return "Insufficient funds or account not found"


# Function to create a new account
def create_account(user_id, name, pin):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts (user_id, name, pin, balance) VALUES (%s, %s, %s, %s)", (user_id, name, pin, 0))
    connection.commit()
    connection.close()
    
    return "Account created successfully"


# Function to delete an account
def delete_account(user_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM accounts WHERE user_id = %s", (user_id,))
    connection.commit()
    connection.close()
    
    return "Account deleted successfully"


# Function to modify account details (e.g., change pin)
def modify_account(user_id, new_name=None, new_pin=None):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="Legendofzeld@10totk",  # Update with your MySQL password
        database="banking_system"
    )
    
    cursor = connection.cursor()
    
    if new_name:
        cursor.execute("UPDATE accounts SET name = %s WHERE user_id = %s", (new_name, user_id))
    
    if new_pin:
        cursor.execute("UPDATE accounts SET pin = %s WHERE user_id = %s", (new_pin, user_id))
    
    connection.commit()
    connection.close()
    
    return "Account modified successfully"


# Main Menu for the banking app
def main_menu():
    print("\nWelcome to the Banking System!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create Account")
    print("5. Delete Account")
    print("6. Modify Account Details")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        user_id = input("Enter your User ID: ")
        print("Balance: ", check_balance(user_id))
    
    elif choice == '2':
        user_id = input("Enter your User ID: ")
        amount = float(input("Enter deposit amount: "))
        print(deposit(user_id, amount))
    
    elif choice == '3':
        user_id = input("Enter your User ID: ")
        amount = float(input("Enter withdrawal amount: "))
        print(withdraw(user_id, amount))
    
    elif choice == '4':
        user_id = input("Enter your new User ID: ")
        name = input("Enter your name: ")
        pin = input("Enter a PIN: ")
        print(create_account(user_id, name, pin))
    
    elif choice == '5':
        user_id = input("Enter your User ID to delete: ")
        print(delete_account(user_id))
    
    elif choice == '6':
        user_id = input("Enter your User ID to modify: ")
        new_name = input("Enter new name (or press enter to skip): ")
        new_pin = input("Enter new PIN (or press enter to skip): ")
        print(modify_account(user_id, new_name, new_pin))
    
    elif choice == '7':
        print("Exiting... Goodbye!")
        return False
    else:
        print("Invalid option, please try again.")
    
    return True


# Running the program
if __name__ == "__main__":
    while main_menu():
        pass
