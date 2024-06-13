#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests

if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    unique_user_ids = list(set([task['userId'] for task in data]))
    user_tasks_dict = {}
    
    for user_id in unique_user_ids:
        user_info = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
        user_tasks = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos').json()
        
        formatted_tasks = [{
            "username": user_info['username'],
            "task": task['title'],
            "completed": task['completed']
        } for task in user_tasks]
        
        user_tasks_dict[user_id] = formatted_tasks

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(user_tasks_dict, file)
