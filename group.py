"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_grouop ={'Jill':{'age': 26, 'job': 'biologist',
                    'relationships': {'friend': ['Zalika'], 'partner':['John']}},
            'Zalika': {'age': 28, 'job': 'artist',
                     'relationships': {'friend': ['Jill'], 'landlord': ['Nash']}},
            'John': {'age': 27, 'job': 'writer',
                     'relationships': {'partner': ['Jill']}},
            'Nash': {'age': 34, 'job': 'chef',
                     'relationships': {'uncle': ['John'], 'employee': ['Zalika']}}
            }