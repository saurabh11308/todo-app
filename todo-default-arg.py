FILEPATH = "todos1.txt"

def get_todos(filepath=FILEPATH):
    """This is the get_todos() routine used to read the todos items from the file todos.txt
    and load it to the todos list variable"""
    with open(filepath) as file:
        todos_arg = file.readlines()
    return todos_arg

def set_todos(todos_arg,filepath=FILEPATH):
    """This is the set_todos routine which takes the modified todos list as argument and stores it in the
    file"""
    with open(filepath,"w") as file:
        file.writelines(todos_arg)
help(set_todos)
help(get_todos)
while True:
    option = input('Add, Show, Edit, Complete or Exit')
    option = option.strip()

    if option.startswith('Add'):
        add_item = option[4:]+'\n'
        todos = get_todos()
        todos.append(add_item)
        set_todos(todos)
    elif option.startswith('Edit'):
        try:
            edit_index = int(option[5:])
            edit_value = input("Enter the new value to be set ")+'\n'
            todos = get_todos()
            todos[edit_index] = edit_value
            set_todos(todos)
        except ValueError:
            print("Please enter integer value of index")
        except IndexError:
            print("Please enter value within index.")
    elif option.startswith('Show'):
        todos = get_todos()
        for index, value in enumerate(todos):
            value = value.strip('\n')
            print(f"{index+1}--{value}")
    elif option.startswith('Complete'):
        try:
            c_index = int(option[9:])
            todos = get_todos()
            todos.pop(c_index)
            set_todos(todos)
        except ValueError:
            print("Please enter integer value to be completed")
        except IndexError:
            print("Please enter value to be completed within range")
    elif option.startswith("Exit"):
        break

print("Bye!!!")

