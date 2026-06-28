user_string = "Enter the option to Add,Show,Edit,Complete or Exit:"
user_string1 = "Enter the item that you want to add"
user_string2 = "Please enter the index that you want to edit"
user_string3 = "Enter the new value to be replaced"
user_string4 = "With edit you need to specify numeric index"
user_string5 = "Please enter a valid option"

while True:
    user_option = input(user_string)
    user_option = user_option.strip()

    if user_option.startswith('add') | user_option.startswith('Add') :
        item = user_option[4:]+'\n'
        with open('todos1.txt') as file:
            todos = file.readlines()
        todos.append(item)
        with open('todos1.txt','w') as file:
            file.writelines(todos)
    elif user_option.startswith('show') | user_option.startswith('Show') :
        with open('todos1.txt') as file:
            todos = file.readlines()
        for index,item in enumerate(todos):
            print(f"{index}-{item.strip('\n')}")
    elif user_option.startswith('edit') | user_option.startswith('Edit') :
        try:
            with open('todos1.txt') as file:
                todos = file.readlines()
            for index,item in enumerate(todos):
                print(f"{index}-{item.strip('\n')}")
            index = int(user_option[5:])
            new_value = input(user_string3) +'\n'
            todos[index-1] = new_value
            with open('todos1.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print(user_string4)
    elif user_option.startswith('complete') | user_option.startswith('Complete') :
        with open('todos1.txt') as file:
            todos = file.readlines()
        for index,item in enumerate(todos):
            print(f"{index}-{item.strip('\n')}")
        index = int(user_option[9:])
        todos.pop(index-1)
        with open('todos1.txt','w') as file:
            file.writelines(todos)
    elif user_option.startswith('exit') | user_option.startswith('Exit') :
        break
    else:
        print(user_string5)