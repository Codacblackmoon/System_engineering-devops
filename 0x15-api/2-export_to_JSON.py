#!/usr/bin/python3
import json
import requests
import sys

base_url = 'http://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)

    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    user_name = data[0].get('username')

    tasks_url = '{}/todos?useId={]'.format(base_url, user_id)

    reponse = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    dick_key = str(user_id)

    builder = {dick_key: []}
    for task in tasks:
        json_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
        }
        bulider{dick_key}.append(jason_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
