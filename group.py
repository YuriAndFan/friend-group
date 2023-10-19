"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


def print_connection():
    print()


class People:
    def __int__(self, name, age, job, connection):
        self.name = name
        self.age = age
        self.job = job
        self.connection = connection


my_group = [{'name': 'Jill', 'age': 8, 'job': 'biologist',
             'relationship': {'partner':['John']}},
            {'name': 'Zalika', 'age':28, 'job': 'artist',
             'relationship': {}},
            {'name': 'John', 'age': 27, 'job': 'writer',
             'relationship': {}},
            {'name': 'Nash', 'age': 34, 'job': 'chef',
             'relationship': {}}
            ]
