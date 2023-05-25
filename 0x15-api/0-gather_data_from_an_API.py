#!/usr/bin/python3
import json
import requests
import sys

base_url = 'http://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)

    response + requests.get(user_url)
    data = response.text
    data = json.loads(data)
    name = data[0].get('name')

    tasks_url = '{}/todos?useId={]'.format(base_url, user_id)

    reponse = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    completed =0
    total_tasks = len(tasks)

    completed_task = []
    for task in task:
        
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with task({}/{}):"
            .format(name, completed, total_tasks))
    fpr task in completed_tasks:
        print("\t {}".format(task.get('title')))
