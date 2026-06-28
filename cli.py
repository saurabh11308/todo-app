from backend import get_todos, set_todos
import time

now = time.strftime("%a - %d - %b - %y %H:%M:%S")
print(f"It is {now}")
while True:
    user_option = input("Add, Show, Edit, Complete or Exit!!!")
    user_option = user_option.strip()

    if user_option.startswith("Add"):
        add_value = user_option[4:] + '\n'
        todos = get_todos()
        todos = todos.append(add_value)
        set_todos(todos)
    elif user_option.startswith("Show"):
        todos = get_todos()
        for index,value in enumerate(todos):
            value = value.strip('\n')
            print(f"{index+1} - {value}")
    elif user_option.startswith("Edit"):
        try:
            edit_index = int(user_option[5:])
            edit_value = input(f"Enter the new value to be placed at index {edit_index}")
            todos = get_todos()
            todos[edit_index] = edit_value + '\n'
            set_todos(todos)
        except ValueError:
            print("Please enter a numeric value to be edited.")
        except IndexError:
            print("The value to be edited should lie within the index range")
    elif user_option.startswith("Complete"):
        try:
            c_index = int(user_option[9:])
            todos = get_todos()
            todos.pop(c_index)
            set_todos(todos)
        except ValueError:
            print("Please enter a numeric value to be completed!")
        except IndexError:
            print("The value to be completed should lie within the index range!")
    elif user_option.startswith("Exit"):
        break
    else:
        print("Please enter a valid option!!")

print("Bye!!!")