import os
path = '/Users/trung/PycharmProjects/pythonProject'
filename = 'test01.py'
with open(os.path.join(path, filename), 'rt') as f:
    content = f.readlines()
print(content)