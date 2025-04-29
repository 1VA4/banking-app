import tkinter as tk
from tkinter import messagebox
from banking_app import check_balance, deposit, withdraw, create_account, delete_account, modify_account, show_all_accounts

class BankingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Banking App")

        # Main Menu
        self.main_menu_frame = tk.Frame(root)
        self.main_menu_frame.pack()

        # Option Buttons
        self.label = tk.Label(self.main_menu_frame, text="Welcome to the Banking App", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.balance_button = tk.Button(self.main_menu_frame, text="Check Balance", command=self.check_balance_screen)
        self.balance_button.pack(pady=5)

        self.deposit_button = tk.Button(self.main_menu_frame, text="Deposit", command=self.deposit_screen)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.main_menu_frame, text="Withdraw", command=self.withdraw_screen)
        self.withdraw_button.pack(pady=5)

        self.create_button = tk.Button(self.main_menu_frame, text="Create Account", command=self.create_account_screen)
        self.create_button.pack(pady=5)

        self.delete_button = tk.Button(self.main_menu_frame, text="Delete Account", command=self.delete_account_screen)
        self.delete_button.pack(pady=5)

        self.modify_button = tk.Button(self.main_menu_frame, text="Modify Account", command=self.modify_account_screen)
        self.modify_button.pack(pady=5)

        self.show_all_button = tk.Button(self.main_menu_frame, text="See All Accounts", command=self.show_all_accounts_screen)
        self.show_all_button.pack(pady=5)

        self.exit_button = tk.Button(self.main_menu_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    # Functions to switch to each screen

    def check_balance_screen(self):
        self.main_menu_frame.pack_forget()
        self.balance_frame = tk.Frame(self.root)
        self.balance_frame.pack()

        self.user_id_label = tk.Label(self.balance_frame, text="Enter User ID:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self.balance_frame)
        self.user_id_entry.pack(pady=10)

        self.balance_button = tk.Button(self.balance_frame, text="Check Balance", command=self.show_balance)
        self.balance_button.pack(pady=5)

        self.back_button = tk.Button(self.balance_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def show_balance(self):
        user_id = self.user_id_entry.get()
        balance = check_balance(user_id)
        messagebox.showinfo("Balance", f"Balance: ${balance}")

    def deposit_screen(self):
        self.main_menu_frame.pack_forget()
        self.deposit_frame = tk.Frame(self.root)
        self.deposit_frame.pack()

        self.amount_label = tk.Label(self.deposit_frame, text="Enter Deposit Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.deposit_frame)
        self.amount_entry.pack(pady=10)

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit_funds)
        self.deposit_button.pack(pady=5)

        self.back_button = tk.Button(self.deposit_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def deposit_funds(self):
        amount = float(self.amount_entry.get())
        user_id = self.user_id_entry.get()
        result = deposit(user_id, amount)
        messagebox.showinfo("Deposit", result)

    def withdraw_screen(self):
        self.main_menu_frame.pack_forget()
        self.withdraw_frame = tk.Frame(self.root)
        self.withdraw_frame.pack()

        self.amount_label = tk.Label(self.withdraw_frame, text="Enter Withdraw Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.withdraw_frame)
        self.amount_entry.pack(pady=10)

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw_funds)
        self.withdraw_button.pack(pady=5)

        self.back_button = tk.Button(self.withdraw_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def withdraw_funds(self):
        amount = float(self.amount_entry.get())
        user_id = self.user_id_entry.get()
        result = withdraw(user_id, amount)
        messagebox.showinfo("Withdraw", result)

    def create_account_screen(self):
        self.main_menu_frame.pack_forget()
        self.create_account_frame = tk.Frame(self.root)
        self.create_account_frame.pack()

        self.user_id_label = tk.Label(self.create_account_frame, text="Enter User ID:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self.create_account_frame)
        self.user_id_entry.pack(pady=5)

        self.name_label = tk.Label(self.create_account_frame, text="Enter Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.create_account_frame)
        self.name_entry.pack(pady=5)

        self.pin_label = tk.Label(self.create_account_frame, text="Enter PIN:")
        self.pin_label.pack(pady=5)
        self.pin_entry = tk.Entry(self.create_account_frame, show="*")
        self.pin_entry.pack(pady=5)

        self.create_button = tk.Button(self.create_account_frame, text="Create Account", command=self.create_account)
        self.create_button.pack(pady=10)

        self.back_button = tk.Button(self.create_account_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def create_account(self):
        user_id = self.user_id_entry.get()
        name = self.name_entry.get()
        pin = self.pin_entry.get()
        result = create_account(user_id, name, pin)
        messagebox.showinfo("Account Created", result)
        self.back_to_main_menu()

    def delete_account_screen(self):
        self.main_menu_frame.pack_forget()
        self.delete_account_frame = tk.Frame(self.root)
        self.delete_account_frame.pack()

        self.user_id_label = tk.Label(self.delete_account_frame, text="Enter User ID to Delete:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self.delete_account_frame)
        self.user_id_entry.pack(pady=10)

        self.delete_button = tk.Button(self.delete_account_frame, text="Delete Account", command=self.delete_account)
        self.delete_button.pack(pady=5)

        self.back_button = tk.Button(self.delete_account_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def delete_account(self):
        user_id = self.user_id_entry.get()
        result = delete_account(user_id)
        messagebox.showinfo("Account Deleted", result)
        self.back_to_main_menu()

    def modify_account_screen(self):
        self.main_menu_frame.pack_forget()
        self.modify_account_frame = tk.Frame(self.root)
        self.modify_account_frame.pack()

        self.user_id_label = tk.Label(self.modify_account_frame, text="Enter User ID to Modify:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self.modify_account_frame)
        self.user_id_entry.pack(pady=10)

        self.new_name_label = tk.Label(self.modify_account_frame, text="Enter New Name (Optional):")
        self.new_name_label.pack(pady=5)
        self.new_name_entry = tk.Entry(self.modify_account_frame)
        self.new_name_entry.pack(pady=5)

        self.new_pin_label = tk.Label(self.modify_account_frame, text="Enter New PIN (Optional):")
        self.new_pin_label.pack(pady=5)
        self.new_pin_entry = tk.Entry(self.modify_account_frame, show="*")
        self.new_pin_entry.pack(pady=5)

        self.modify_button = tk.Button(self.modify_account_frame, text="Modify Account", command=self.modify_account)
        self.modify_button.pack(pady=10)

        self.back_button = tk.Button(self.modify_account_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def modify_account(self):
        user_id = self.user_id_entry.get()
        new_name = self.new_name_entry.get()
        new_pin = self.new_pin_entry.get()
        result = modify_account(user_id, new_name, new_pin)
        messagebox.showinfo("Account Modified", result)
        self.back_to_main_menu()

    def show_all_accounts_screen(self):
        self.main_menu_frame.pack_forget()
        self.all_accounts_frame = tk.Frame(self.root)
        self.all_accounts_frame.pack()

        accounts = show_all_accounts()
        text = "\n".join([f"User ID: {a[0]}, Name: {a[1]}, PIN: {a[2]}, Balance: ${a[3]:.2f}" for a in accounts])

        self.accounts_label = tk.Label(self.all_accounts_frame, text=text, justify="left", font=("Courier", 10))
        self.accounts_label.pack(pady=10)

        self.back_button = tk.Button(self.all_accounts_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def back_to_main_menu(self):
        # Clear all frames and go back to the main menu
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.main_menu_frame.pack()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()
