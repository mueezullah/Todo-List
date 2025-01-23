def main():
    # Initialize an empty list to store tasks.
    tasks = []
    print("\n---To Do List---")
    while True:
        # Display the main menu
        print("\nChoice you want to select")
        print("1. Add Tasks")
        print("2. Show Tasks")
        print("3. Mark Tasks as Completed")
        print("4. Remove Tasks")
        print("5. Exit")

        # User's Choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Add tasks to list
            print()
            n_tasks = int(input("How many tasks you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "Completed": False})
                print("ADDED!")

        elif choice == '2':
            #Displaying all tasks with their current status
            print("\n Tasks")

            for index, task in enumerate(tasks):
                status = "Completed" if task["Completed"] else "Pending..."
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            # Mark task as Completed
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid Task number.")

        elif choice == '4':
            # Remove task from the list
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_tasks = tasks.pop(task_index)
                print(f"Task '{removed_tasks['task']}' removed!")
            else:
                print("Invalid Task number.")


        elif choice == '5':
            # Exit the program
            print("Goodbye! Stay productive!")
            print("------------Exit------------")
            break


        else:
            # Error handling for invalid choices
            print("Invalid Choice. Please try again.")



if __name__ == "__main__":
    main()