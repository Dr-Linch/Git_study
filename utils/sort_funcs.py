import os
import json

with open(os.path.join('data', 'posts.json'), 'rt', encoding='utf-8') as json_file:
    data = json.load(json_file)

users_info: dict = {'users': []}
users_keys = ['id', 'title']

for item in data:
    short_info: dict = {}
    for key in users_keys:
        short_info[key] = item[key]

    users_info['users'].append(short_info)

for user in users_info['users']:
    print('\n')
    for key, value in user.items():
        print(f'{key}: {value}')

print('first commit 1')
print('seccond commit 2')