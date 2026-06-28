from backend import get_todos,set_todos
import FreeSimpleGUI as fsg

label = fsg.Text("Add a new todo: ")
input_box = fsg.InputText(tooltip="Enter a todo :-")
add_button = fsg.Button("Add")

window = fsg.Window("My todo App", layout=[[label,input_box,add_button]])
window.read()
window.close()