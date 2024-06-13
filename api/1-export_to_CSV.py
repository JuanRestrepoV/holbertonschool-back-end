#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
and exports the data to a CSV file.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    ID_NUMBER = int(argv[1])
    
    user_url = f'https://jsonplaceholder.typicode.com/users/{ID_NUMBER}'
    employee_data = requests.get(user_url).json()
    employee_username = employee_data.get("username")
    
    todos_url = f'https://jsonplaceholder.typicode.com/users/{ID_NUMBER}/todos'
    employee_todos = requests.get(todos_url).json()
    
    file_name = f'{ID_NUMBER}.csv'
    
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for todo in employee_todos:
            csv_writer.writerow([ID_NUMBER, employee_username,
                                 todo["completed"], todo["title"]])
            