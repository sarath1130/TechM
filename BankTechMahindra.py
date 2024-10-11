import random

class Bank:
    def create_account(self):
        self.account_holder_name = input('\t\tEnter your name: ')
        self.contact_num = input('\t\tEnter Contact Number: ')
        self.balance = 0
        self.acc_type = input("\t\tAccount Types: \n\t\t1. Savings Account \n\t\t2. Current Account \n\t\t3. Business Account \nEnter Account Type: ")
        self.acc_number = int(random.random() * 10000)  
        self.withdraw_count = 0
        self.deposit_count = 0
        print('\nYour Account Number is:', self.acc_number)

    def print_details(self):
        print('\nYour Account Details:')
        print('\tAccount Number:', self.acc_number)
        print('\tAccount Holder Name:', self.account_holder_name)
        print('\tAccount Type:', self.acc_type)
        print('\tYour Account Balance:', self.balance)
        print('\tContact Number:', self.contact_num)

    def deposit(self):
        print('\nDeposit Successful.')
        print('\tAvailable Balance is:', self.balance)

    def withdraw(self):
        print('\nWithdrawal Successful.')
        print('\tAvailable Balance is:', self.balance)

    def statement(self):
        print('\nYour Transaction Amount:')
        print('\tTotal Deposits:', self.deposit_count)
        print('\tTotal Withdrawals:', self.withdraw_count)
        print('\tTotal Available Balance:', self.balance)

bank_accounts = {}

while True:
    print('\nHow Can I Help You:')
    print('\t\t1. Create Account')
    print('\t\t2. View Account Details By Account Number')
    print('\t\t3. Deposit')
    print('\t\t4. Withdraw')
    print('\t\t5. Fund Transfer')
    print('\t\t6. Statement')
    print('\t\t7. Exit')
    
    user_choice = int(input('Enter your Choice: '))

    if user_choice == 1:
        new_account = Bank()
        new_account.create_account()
        bank_accounts[new_account.acc_number] = new_account

    elif user_choice == 2:
        account_num = int(input('\t\tEnter your Account Number: '))
        if account_num not in bank_accounts:
            print('Account is Not Present in our Bank. Please, Enter a Valid Account Number.')
        else:
            temp_account = bank_accounts[account_num]
            temp_account.print_details()

    elif user_choice == 3:
        account_num = int(input('\t\tEnter your Account Number: '))
        if account_num not in bank_accounts:
            print('Account is Not Present in our Bank. Please, Enter a Valid Account Number.')
        else:
            temp_account = bank_accounts[account_num]
            amount = int(input('\t\tEnter the Amount to Deposit: '))
            temp_account.balance += amount
            temp_account.deposit_count += 1
            temp_account.deposit()

    elif user_choice == 4:
        account_num = int(input('\t\tEnter your Account Number: '))
        if account_num not in bank_accounts:
            print('Account is Not Present in our Bank. Please, Enter a Valid Account Number.')
        else:
            temp_account = bank_accounts[account_num]
            amount = int(input('\t\tEnter the Amount to Withdraw: '))
            if temp_account.balance >= amount:
                temp_account.balance -= amount
                temp_account.withdraw_count += 1
                temp_account.withdraw()
                print('Transaction Successful.')
            else:
                print('Insufficient Funds.')

    elif user_choice == 5:
        sender_acc_num = int(input('\t\tEnter Sender\'s Account Number: '))
        receiver_acc_num = int(input('\t\tEnter Receiver\'s Account Number: '))
        if sender_acc_num not in bank_accounts or receiver_acc_num not in bank_accounts:
            if sender_acc_num not in bank_accounts:
                print("Sender's Account is Not Present in our Bank. Please, Enter a Valid Account Number.")
            if receiver_acc_num not in bank_accounts:
                print("Receiver's Account is Not Present in our Bank. Please, Enter a Valid Account Number.")
        else:
            sender_account = bank_accounts[sender_acc_num]
            receiver_account = bank_accounts[receiver_acc_num]
            amount = int(input('\t\tEnter the Amount to Send: '))
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                sender_account.withdraw_count += 1
                receiver_account.balance += amount
                receiver_account.deposit_count += 1
                print('Transaction Successful.')
            else:
                print('Insufficient Funds.')
            sender_account.print_details()
            receiver_account.print_details()

    elif user_choice == 6:
        account_num = int(input('\t\tEnter your Account Number: '))
        if account_num not in bank_accounts:
            print('Account is Not Present in our Bank. Please, Enter a Valid Account Number.')
        else:
            temp_account = bank_accounts[account_num]
            temp_account.statement()

    elif user_choice == 7:
        break
