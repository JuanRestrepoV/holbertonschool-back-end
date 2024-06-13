#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = int(argv[1])
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    username = user_response.json().get('username')
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    user_tasks = [
        task for task in todos_response.json() if task.get('userId') == user_id
    ]

    tasks_json = [{
        "task": task['title'],
        "completed": task['completed'],
        "username": username
    } for task in user_tasks]

    json_data = {str(user_id): tasks_json}
    with open(f"{user_id}.json", "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
