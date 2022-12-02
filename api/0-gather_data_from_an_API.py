#!/usr/bin/python3
''' *** *** '''


if __name__ == '__main__':
    from requests import get
    from sys import argv

    rq = get('https://jsonplaceholder.typicode.com/users/')
    rq_name = rq.json()

    rq = get('https://jsonplaceholder.typicode.com/todos/')
    rq_data = rq.json()

    done = total = 0

    for i in rq_name:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')
    
    for task in rq_data:
        if task.get('userId') == int(argv[1]):
            total += 1
            if task.get('completed'):
                done += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(rq_name, done, total))
    for task in rq_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
