import os

directory = '0x06-python-classes'

for filename in os.listdir(directory):
    if filename.endswith('.py'):
        with open(os.path.join(directory, filename), 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('#!/usr/bin/python3\n' + content)