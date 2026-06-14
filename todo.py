import os

TASKS_FILE = "tasks.txt"

class Task:

    def __init__(self, description, is_done=False):
        self.description = description
        self.is_done = is_done

    def mark_complete(self):
        self.is_done = True

    def to_string(self):
        return f"{self.description}|{self.is_done}"

    @classmethod
    def from_string(cls, line):
        description, is_done_str = line.split("|")
        is_done = is_done_str == "True"
        return cls(description, is_done)
    

def save_tasks(tasks_list):
    with open(TASKS_FILE, "w") as file:
        for task in tasks_list:
            text_line = task.to_string()
            file.write(text_line + "\n")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    loaded_tasks = []
    with open(TASKS_FILE, "r") as file:
        for line in file:
            task_obj = Task.from_string(line)
            loaded_tasks.append(task_obj)
    return loaded_tasks

def main():
    tasks = load_tasks()

    while True:
        print("/n--- CURRENT TO-DO LIST ---")
        if not tasks:
            print("No tasks yet! Choose option 1 to add one.")
        else:
            for index, t in enumerate(tasks, start=1):
                status = "✅" if t.is_done else "❌"
                print(f"{index}. [{status}] {t.description}")
            print("-------------------------------")

            
        print(f"\nOptions: [1] Add Task | [2] Complete Task | [3] Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            desc = input("What is the description of the task? ")
            new_task = Task(desc)
            tasks.append(new_task)
            save_tasks(tasks)

        elif choice == "2":
            target = input("Enter the exact description of the task you want to complete: ")
            for t in tasks:
                if t.description == target:
                    t.mark_complete()
                    save_tasks(tasks)
                    print("Task completed!")


        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2 or 3. ")

if __name__ == "__main__":
    main()