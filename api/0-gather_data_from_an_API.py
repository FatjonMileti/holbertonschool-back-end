#!/usr/bin/python3
''' *** *** '''


if __name__ == '__main__':
    from requests import get
    from sys import argv

    rq_users = get('https://jsonplaceholder.typicode.com/users/{}'.
                   format(argv[1])).json()

    rq_name = rq_users.get('name')

    rq_data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                  format(argv[1])).json()

    done = total = 0

    for tasks in rq_data:
        total += 1
        if tasks.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(rq_name, done, total))

    for task in rq_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
