#!/usr/bin/python3
''' *** *** '''


if __name__ == '__main__':
    from requests import get
    from sys import argv

    rq = get('https://jsonplaceholder.typicode.com/users/{}'.
             format(argv[1]))
    rq_name = rq.json().get('name')

    rq = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
             format(argv[1]))
    rq_data = rq.json()
    done = total = 0
    for task in rq_data:
        total += 1
        if task.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(rq_name, done, total))
    for task in rq_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
