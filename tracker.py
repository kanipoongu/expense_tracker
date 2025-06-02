from datetime import datetime
import csv
import os

def add_expense():
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

    




def view_expense():
    with open('expenses.csv','r') as f:
        reader = csv.DictReader(f)
        print(f"{'Description':<20}{'Amount':>10}{'Date':^12}")
        for row in reader:
            print(f"{row['Description']:<20}{row['Amount']:>10}{row['Date']:^12}")

# add_expense()
view_expense()