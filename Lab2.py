import json
from random import randint, choice
from pprint import pprint

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

class Birthday:
    def __init__(self):
        self.year = randint(2000, 2022)
        self.month = choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        self.day = randint(1, 31)

data = {
    'Birthdays': []
}

for i in range(50):
    data['Birthdays'].append(Birthday().__dict__)

#write(data, 'data1.json')

n_data = read('data1.json')

print(n_data['Birthdays'][49])

g = Birthday()
g.name = n_data['Birthdays'][0]['month']

print(g.name)
input()