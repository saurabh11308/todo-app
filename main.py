print("Todo")
user_name = input()
print(user_name)

#Another way of doing the same thing is

user_text = input("Enter the todo")
print(user_text)

# Basically input is a function which is capable of taking inputs as well as printing output

#Another way of doing the same thing is holding the input string in a variable and printing it

prompt = "Enter a todo"
user_text = input(prompt)
user_text1 = input(prompt)
user_text2 = input(prompt)
user_text3 = input(prompt)

do_list = [user_text,user_text1,user_text2,user_text3]
print(user_text)
print(do_list)
print(type(do_list))
print(type(1))