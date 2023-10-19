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


my_group0 = [{'name': 'Jill', 'age': 8, 'job': 'biologist',
             'relationship': {'partner':['John']}},
            {'name': 'Zalika', 'age':28, 'job': 'artist',
             'relationship': {'friends':['Jill']}},
            {'name': 'John', 'age': 27, 'job': 'writer',
             'relationship': {'partner': ['Jill']}},
            {'name': 'Nash', 'age': 34, 'job': 'chef',
             'relationship': {'cousin':['John'], 'landlord':['Zalika']}}
            ]




my_grouop1 ={'Jill':{'age': 8, 'job': 'biologist',
                    'relationships': {'partner': ['John']}},
            'Zalika': {'age': 28, 'job': 'artist',
                     'relationships': {'friends': ['Jill']}},
            'John': {'age': 27, 'job': 'writer',
                    'relationships': {'partner': ['Jill']}},
            'Nash': {'age': 34, 'job': 'chef',
                    'relationships': {'cousin':['John'], 'landlord':['Zalika']}}
            }