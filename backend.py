FILEPATH = 'todos1.txt'


def get_todos(filepath = FILEPATH):
    """This routine is used to read the todos items from the file present in FILEPATH and return the corresponding list"""
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def set_todos(todos_local, filepath = FILEPATH):
    """This routine takes the todos_local list of todos and writes them to the file"""
    with open(filepath,'w') as file:
        file.writelines(todos_local)

print(__name__)
if __name__ == "__main__":
    print(get_todos())
    help(get_todos)
    help(set_todos)