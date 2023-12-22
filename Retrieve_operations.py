import sqlite3

class RetreiveManager:
    def __init__(self, database_name='expenditure.db'):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        

    
    def retrieve_data(self):
        self.cursor.execute('SELECT * FROM expenditures')
        rows = self.cursor.fetchall()

        groups = {}
        for row in rows:
            date, group_name, person, expenditure = row[1], row[2], row[3], row[4]

            if date not in groups:
                groups[date] = {'name': group_name, 'participants': {}}
            if person not in groups[date]['participants']:
                groups[date]['participants'][person] = 0
            groups[date]['participants'][person] += expenditure

        return groups

    
if __name__ == "__main__":
    retreive_manager = RetreiveManager()
    data = retreive_manager.retrieve_data()
    print(data)
