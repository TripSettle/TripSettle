import sqlite3
from datetime import datetime
 
def create_table():
    connection = sqlite3.connect('expenditure.db')
    cursor = connection.cursor()
 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenditures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            group_name TEXT,
            person TEXT,
            expenditure REAL
        )
    ''')
 
    connection.commit()
    connection.close()
 
def insert_data(date, group_name, person, expenditure):
    connection = sqlite3.connect('expenditure.db')
    cursor = connection.cursor()
 
    cursor.execute('''
        INSERT INTO expenditures (date, group_name, person, expenditure)
        VALUES (?, ?, ?, ?)
    ''', (date, group_name, person, expenditure))
 
    connection.commit()
    connection.close()

from transaction_operations import create_table, insert_data
from datetime import datetime
 
# ... (other functions remain the same)
 
def main():
    create_table()
 
    try:
        while True:
            date = input("Enter the date (YYYY-MM-DD) or 'q' to quit: ")
            if date.lower() == 'q':
                break
            group_name = input("Enter the name of the group: ")
            total_amount = float(input("Enter the total expenditure for the group: "))
            num_people = int(input("Enter the number of people in the group: "))
            if num_people <= 0:
                print("Number of people must be greater than 0. Exiting.")
                break
            for i in range(num_people):
                person = input(f"Enter the name of person {i+1}: ")
                expenditure = float(input(f"Enter the expenditure for {person}: "))
                insert_data(date, group_name, person, expenditure)
 
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
 
if __name__ == "__main__":
    main()
