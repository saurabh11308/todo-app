def get_todos():
    with open('file.txt') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(todos_local):
    with open('file.txt','w') as file:
        file.writelines(todos_local)

while True:
    user_option = input('Add,Show,Edit,Complete or Exit')
    user_option = user_option.strip()

    if user_option.startswith('Add'):
        add_item = user_option[4:]+'\n'
        todos = get_todos()
        todos.append(add_item)
        set_todos(todos)
    elif user_option.startswith('Show'):
        todos = get_todos()
        for index,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")
    elif user_option.startswith('Edit'):
        try:
            edit_index = int(user_option[5:])
            todos=get_todos()
            edit_val=input(f"Enter the new value at index{edit_index}")
            todos[edit_index]=edit_val
            set_todos(todos)
        except ValueError:
            print('Please enter a numeric value to edit')
        except IndexError:
            print('Please enter the value to be edited within range')
    elif user_option.startswith('Complete'):
        try:
            c_index = int(user_option[9:])
            todos=get_todos()
            todos.pop(c_index)
            set_todos(todos)
        except ValueError:
            print('Please enter a numeric value to complete')
        except IndexError:
            print('Please enter the value to be completed within range')
    elif user_option.startswith('Exit'):
        break
    else:
        print("Please enter a valid option")

exit("Bye!!!")