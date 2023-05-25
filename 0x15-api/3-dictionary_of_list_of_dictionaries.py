#!/usr/bin/python3
import json
import requests

base_url = 'http://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)

    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    
    builder = {}
    for user in data:
        user_id = user.get('id')

        user_name = user.get('username')

        dick_key = str(user_id)

        builder[dick_key] = []
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

        response = requests.get(tasks_url)
        tasks = response.text
        tasks = json.loads(tasks)

        for task in tasks:
            json_data = {
                    "task": task['title'],
                    "completed": task['completed']
                    "username": user_name
            )
            builder[dick_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
