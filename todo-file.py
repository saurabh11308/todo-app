user_string = "Enter the option to Add,Show,Edit,Complete or Exit:"
user_string1 = "Enter the item that you want to add"
user_string2 = "Please enter the index that you want to edit"
user_string3 = "Enter the new value to be replaced"
user_string4 = "Enter the index that you want to delete"
user_string5 = "Please enter a valid option"


while True:
    option = input(user_string)
    match option.strip():
        case 'Add'|'add'|'ADD':
            item = input(user_string1) + '\n'
            with open('todos.txt') as file:
                todos = file.readlines()
            todos.append(item)
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'Show'|'show'|'SHOW':
            with open('todos.txt') as file:
                todos = file.readlines()
            todos = [item.strip('\n') for item in todos]
            for index,item in enumerate(todos):
                print(f"{index+1}--{item}")
        case 'edit'|'Edit'|'EDIT':
            with open('todos.txt') as file:
                todos = file.readlines()
            todos1 = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos1):
                print(f"{index + 1}--{item}")
            edit_index = int(input(user_string2))
            new_value = input(user_string3) + '\n'
            todos[edit_index-1] = new_value
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'complete'|'Complete'|'COMPLETE':
            with open('todos.txt') as file:
                todos = file.readlines()
            todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                print(f"{index + 1}--{item}")
            del_index = int(input(user_string4))
            todos.pop(del_index-1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'exit'|'Exit':
            break
        case _:
            print(user_string5)


print("Bye!!!")