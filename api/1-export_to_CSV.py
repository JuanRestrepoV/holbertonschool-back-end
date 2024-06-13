#!/usr/bin/python3
"""
Module that exports data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = int(argv[1])
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    username = user_response.json().get('username')

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos')
    user_tasks = [
        task for task in todos_response.json() if task.get('userId') == user_id
    ]

    with open(f"{user_id}.csv", 'a', newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, dialect="unix")
        for task in user_tasks:
            csv_writer.writerow([
                task['userId'], username,
                task['completed'], task['title']
            ])
