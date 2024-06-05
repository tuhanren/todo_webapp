FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
        to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


""" __name__ is the name of the current module or file
    if a module is executed directly, then __name__ is __main__
    if a module is imported into another module and executed, then __name__ is this module's name (functions) instead
    This can be used for testing purpose like the code below
"""
if __name__ == "__main__":
    print("Hello from function.py directly, testing purpose")
    print(get_todos())
