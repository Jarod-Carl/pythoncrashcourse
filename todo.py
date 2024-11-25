# go through existing todos, listing each one, asking the user if the completed it
#if they completed it, remove it from the list, if not, keep it on the list

#ask the user to add more todos
#allow them to quit out when they are done adding their todos

with open("todo_list.txt", "r") as f:
    content = f.read()
    #print(content.split("\n"))

    todo_list = content.split("\n")

    remaining_todo_list = []
    
    for todo in todo_list:
        print(todo)
        user_input = input("completed? (y/n)")
        if user_input != "y":
            remaining_todo_list.append(todo)

    while True:
        new_todo = input("Add todo (q to quit)")
        if new_todo == "q":
            break
        else:
            remaining_todo_list.append(new_todo)

with open("todo_list.txt", "w") as f:
    output = "\n".join(remaining_todo_list)
    f.write(output)

    

