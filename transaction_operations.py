import sqlite3
from datetime import datetime

class ExpenditureManager:
    def __init__(self, database_name='expenditure.db'):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenditures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                group_name TEXT,
                person TEXT,
                expenditure REAL
            )
        ''')
        self.connection.commit()

    def insert_data(self, date, group_name, person, expenditure):
        self.cursor.execute('''
            INSERT INTO expenditures (date, group_name, person, expenditure)
            VALUES (?, ?, ?, ?)
        ''', (date, group_name, person, expenditure))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

def main():
    expenditure_manager = ExpenditureManager()

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
                expenditure_manager.insert_data(date, group_name, person, expenditure)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    finally:
        expenditure_manager.close_connection()

if __name__ == "__main__":
    main()
