import streamlit as st
from backend import get_todos,set_todos

todos = get_todos()

def add_todo():
    todo = st.session_state["add_todo"] + '\n'
    todos.append(todo)
    set_todos(todos)

st.title("Hello World")
st.subheader("This is a todo app")
st.write("This app is used to make everyday life simple!!!")

for index,todo in enumerate(todos):
    flag = st.checkbox(todo,key=index)
    if flag:
        todos.pop(index)
        set_todos(todos)


st.text_input(label="Add a todo :",placeholder="Enter text here: ",key="add_todo",on_change=add_todo)

print("Hello 123 !!!")
print(st.session_state)