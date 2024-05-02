#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    ID_NUMBER = int(argv[1])
    employee_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            ID_NUMBER)).json()
    employee_name = employee_data.get("name")
    employee_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            ID_NUMBER)).json()
    total_num_todos = len(employee_todos)
    count_completed_todos = 0
    for todo in employee_todos:
        if todo["completed"] is True:
            count_completed_todos += 1
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, count_completed_todos, total_num_todos))
    for todo in employee_todos:
        if todo["completed"] is True:
            print("\t " + todo.get("title"))
