import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)






st.title('My Todo App')
st.subheader('This is my Todo app')
st.subheader('This app is to increase your productivity')

st.text_input(label="",placeholder="Add new Todo", on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st._rerun()


st.session_state