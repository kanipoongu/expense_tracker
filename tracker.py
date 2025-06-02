from datetime import datetime
import csv
import os

def add_expense():
    try:
        description = input('Description for expense:') or 'food'
        amount_input = input('Spent amount in rupees:')
        amount = round(float(amount_input),2) if amount_input else 100.0
        date_str = input('Date in format (YYYY-MM-DD):') 
        # print(description)
        # print(amount)
        if date_str:
            date = datetime.strptime(date_str,"%Y-%m-%d")
        else:
            date = datetime.today()

        # print(date)
        date_formatted = datetime.strftime(date,"%Y-%m-%d")
        # print(date_formatted)
        file_exists = os.path.exists('expenses.csv')
        write_header = not file_exists or os.path.getsize('expenses.csv') == 0
        with open('expenses.csv','a',newline='') as f:
            fieldnames =['Description','Amount','Date']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerow({'Description':description,'Amount':amount,'Date':date_formatted})
        print('Expense added successfully')
    except Exception as e:
        print(f'Exception: {e}')

def view_expense():
    try:
        with open('expenses.csv','r') as f:
            reader = csv.DictReader(f)
            print(f"{'Description':<20}{'Amount':>10}{'Date':^12}")
            for row in reader:
                print(f"{row['Description']:<20}{row['Amount']:>10}{row['Date']:^12}")
    except Exception as e:
        print(f'Exception: {e}')

def show_summary():
    try:
        with open('expenses.csv','r') as f:
            reader = csv.DictReader(f)
            # print(f"{'Description':<20}{'Amount':>10}{'Date':^12}")
            total_day = 0.0
            total_month = 0.0
            for row in reader:
                # print(row)
                amount = float(row['Amount'])
                date = row['Date']
                date_object = datetime.strptime(date,'%Y-%m-%d')
                # print(date_object)
                month_no = date_object.month
                # print(date)
                today_dt = datetime.today()
                # print(today_dt)
                month = today_dt.month
                # print(month)
                
                today = today_dt.strftime('%Y-%m-%d')
                # print(today)
                if date == today:
                    total_day += amount
                # print(total_day)
                if month_no == month:
                    total_month += amount
        print(f'The total daily expense is {total_day}')
        print(f'The total monthly expense is {total_month}')
    except Exception as e:
        print(f'Exception: {e}')

def end():
    print('Thank you for using the expense tracker.')
    exit()

def menu():
    while True:
        print(f'\nWelcome to CLI Expense Tracker!')
        menu_dict = {1: 'Add Expense' ,2: 'View Expenses' ,3 :'Show Summary', 4:  'Exit'}
        for index,menu in menu_dict.items():
            print(f'{index}. {menu}')
        choice = int(input('Enter your choice:'))
        # print(choice)
        if choice:
            match choice:
                case 1 :
                    add_expense()
                case 2 :
                    view_expense()
                case 3 :
                    show_summary()
                case 4 :
                    end()
                case _ :
                    print('Please provide a valid input between 1 to 4')
        else:
            print('Please enter a valid choice')


menu()
# add_expense()
# view_expense()

# show_summary()
# end()
