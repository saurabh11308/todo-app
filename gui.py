from backend import get_todos,set_todos
import FreeSimpleGUI as fsg

label = fsg.Text("Add a new todo: ")
input_box = fsg.InputText(tooltip="Enter a todo :-",key = "ibox")
add_button = fsg.Button("Add")

window = fsg.Window("My todo App", layout=[[label,input_box,add_button]])

event, value = window.read()
#print(event, index)
while True:
    match event:
        case "Add":
            add_item = value["ibox"] + '\n'
            todos = get_todos()
            todos.append(add_item)
            set_todos(todos)
            break
        case "Edit":
            break
        case "Complete":
            break
        case "Exit":
            break

window.close()