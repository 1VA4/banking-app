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
        return "No account by that name"


# Function to deposit funds into an account
def deposit(user_id, amount):
    if amount <= 0:
        return "Deposit must be positive"
    
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
    
    return "Deposit success!!"


# Function to withdraw funds from an account
def withdraw(user_id, amount):
    if amount <= 0:
        return "Withdraw amount must be positive"
    
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
        return "not enough money or account not found"


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
    
    return "Account created"


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
    
    return "Account deleted"


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
    
    return "Account modified"

def show_all_accounts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Legendofzeld@10totk",
        database="banking_system"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    connection.close()
    
    print("\nAll Accounts:")
    for row in rows:
        print(f"User ID: {row[0]}, Name: {row[1]}, PIN: {row[2]}, Balance: ${row[3]:.2f}")


# Main Menu for the banking app
def main_menu():
    print("\nWelcome to the banking app")
    print("1: Check Balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Create Account")
    print("5: Delete Account")
    print("6: Modify Account")
    print("7: See All Accounts")
    print("8: Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        user_id = input("Enter your ID: ")
        print("Balance: ", check_balance(user_id))
    
    elif choice == '2':
        user_id = input("Enter your ID: ")
        amount = float(input("Enter deposit amount: "))
        print(deposit(user_id, amount))
    
    elif choice == '3':
        user_id = input("Enter your ID: ")
        amount = float(input("Enter withdraw amount: "))
        print(withdraw(user_id, amount))
    
    elif choice == '4':
        user_id = input("Enter your new ID: ")
        name = input("Enter your name: ")
        pin = input("Enter a PIN: ")
        print(create_account(user_id, name, pin))
    
    elif choice == '5':
        user_id = input("Enter your ID to delete: ")
        print(delete_account(user_id))
    
    elif choice == '6':
        user_id = input("Enter your ID to modify: ")
        new_name = input("Enter name (or press enter to skip): ")
        new_pin = input("Enter PIN (or press enter to skip): ")
        print(modify_account(user_id, new_name, new_pin))
    
    elif choice == '7':
        show_all_accounts()

    elif choice == '8':
        print("exited")
        return False
    else:
        print("Invalid. try again.")
    
    return True


# Running the program
if __name__ == "__main__":
    while main_menu():
        pass
