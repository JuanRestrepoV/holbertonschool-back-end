#!/usr/bin/python3
"""
Module that export data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    id = int(argv[1])
    emp_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    usr_name = emp_data.json().get('username')
    tasks_data = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    data_all = [boole for boole in tasks_data.json()
                if boole.get('userId') == id]

    with open(f"{id}.csv", 'a', newline='', encoding="utf-8") as csvfile:
        write = csv.writer(csvfile, dialect="unix")
        for data in data_all:
            write.writerow([data['userId'], usr_name,
                            data['completed'], data['title']])
