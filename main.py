completed = []
tasks = []

print("=============================")
print("        TASK MANAGER")
print("=============================")
while True:
    #options menu
    print("\n 1) Insert a task")
    print(" 2) See list of tasks")
    print(" 3) Remove a task")
    print(" 4) Mark a task as completed")
    print(" 5) Clear completed tasks")
    print(" 6) Stop")
    
    option = int(input("\nInsert the option number: "))
    #inserting a new task
    if option == 1:
        new_task = input("Insert a new task: ")
        tasks.append(new_task)
    
    #printing all the tasks
    elif option == 2:
        print("\nPending Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. [ ] {task}")
        print("\nCompleted Tasks:")
        for idx, task in enumerate(completed, start=1):
            print(f"{idx}. [X] {task}")
    #deleting a task
    elif option == 3:
        if tasks:
            index = int(input("Insert the number of the task to be removed: "))
            if index > 0 and index <= len(tasks):
                del tasks[index - 1]
            else:
                print("Invalid task number")
        else:
            print("No tasks to remove")
    #mark a task as completed
    elif option == 4:
        if tasks:
            idx = int(input("Insert the number of the task to be marked as completed: "))
            if idx > 0 and idx <= len(tasks):
                completed.append(tasks.pop(idx - 1))
            else:
                print("Invalid task number")
        else:
            print("No tasks to mark as completed")
    #clear all tasks completed
    elif option == 5:
        completed.clear()
        print("Completed tasks have been cleared")
    #stop program
    elif option == 6:
        break
    else:
        print("Invalid option")

print("Hope you come back soon :)")
