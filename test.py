import project
import csv
import re


class ToDoList:
    def __init__(self, title, priority, type, details):
        self.title = title
        self.priority = priority
        self.type = type
        self.details = details

    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Type: {self.type} \n{self.details}"


todo_list = []
titles = []
commands = ["help", "list", "add", "change", "export", "import", "exit", "remove"]


def todo():
    opening()
    while True:
        command = input("Command: ").lower().strip()
        take_input(command)


def take_input(command):
    if command not in commands:
        print('Enter a valid command ("help" to see commands)')
    elif command == "add":
        add()
    elif command == "help":
        help()
    elif command == "exit":
        exit()
    elif command == "list":
        list()
    elif command == "change":
        change()
    elif command == "export":
        export()
    elif command == "import":
        import_file()
    else:
        remove()


def add():
    while True:
        info = input("Input the title, priority, and type for the list entry: ").strip()
        try:
            title, priority, type = info.split(", ")
        except ValueError:
            print(
                "Title, Priority, and Type must all be present and separated by commas"
            )
            continue
        if title.strip().lower() in titles:
            print("This title already exists")
            continue
        try:
            if not 1 <= int(priority) <= 10:
                print("Priority must be a 1 - 10 int")
                continue
        except ValueError:
            print("Priority must be a 1 - 10 int")
            continue
        break

    while True:
        details = input("Input the details for the entry: ").strip()
        if not details:
            print("Details not present")
            continue
        break

    todo_list.append(
        ToDoList(title.strip(), int(priority.strip()), type.strip(), details.strip())
    )
    titles.append(title.strip().lower())


def change():
    items = ["title", "priority", "type", "details"]
    # Get title to change and type to change and validate them
    while True:
        print(
            "Input the title of the item you want to change and which type you want to change (title, priority, type, details)"
        )
        try:
            change_title, change_type = input().split(", ")
        except ValueError:
            print("Items must both exist and be separated by commas")
            continue
        if change_title.lower().strip() not in titles:
            print("Invalid title")
            continue
        elif change_type.lower().strip() not in items:
            print("Invalid item type. Use 'title', 'priority', 'type', or 'details'")
            continue
        break
    # Loop over the list to find item to change
    pos = 0
    while pos < len(todo_list):
        if (todo_list[pos].title).lower().strip() == change_title.lower().strip():
            break
        else:
            pos += 1
    # Get new value, validate it, and change it
    while True:
        new_value = input("New value: ")
        if new_value == "":
            print("Value not present")
            continue
        elif change_type.lower().strip() == "title":
            if new_value.lower().strip() in titles:
                print("Title already used")
                continue
            todo_list[pos].title = new_value.strip()
            titles.remove(change_title.lower().strip())
            titles.append(new_value.lower().strip())
            break
        elif change_type.lower().strip() == "priority":
            try:
                if not 1 <= int(new_value) <= 10:
                    print("Priority must be an integer from 1 - 10")
                    continue
            except ValueError:
                print("Priority must be an integer from 1 - 10")
                continue
            todo_list[pos].priority = int(new_value.lower().strip())
            break
        elif change_type.lower().strip() == "type":
            todo_list[pos].type = new_value.strip()
            break
        else:
            todo_list[pos].details = new_value.strip()
            break


def export():
    pattern = r"\w+\.csv"
    while True:
        filename = input("File name (ending in .csv): ")
        check = re.match(pattern, filename)
        if not check:
            print("Invalid file name")
            continue
        break
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "priority", "type", "details"]
        )
        writer.writeheader()
        for row in todo_list:
            writer.writerow(
                {
                    "title": row.title,
                    "priority": row.priority,
                    "type": row.type,
                    "details": row.details,
                }
            )
    print("File exported!")


def import_file():
    global todo_list
    global titles
    while True:
        print(
            "Do you want to delete current list and override with new list (override) or add items from new list to current list (add)?"
        )
        response = input("override / add: ")
        if response.strip().lower() == "override":
            todo_list.clear()
            titles.clear()
            break
        elif response.lower().strip() != "add":
            print('Reponse must be "override" or "add"')
            continue
        else:
            break
    pattern = r"\w+\.csv"
    while True:
        filename = input("File name (ending in .csv): ")
        check = re.match(pattern, filename)
        if not check:
            print("Invalid file name")
            continue
        try:
            f = open(filename, "r")
            f.close()
        except FileNotFoundError:
            print("File not found")
            continue
        break
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            todo_list.append(
                ToDoList(
                    row["title"], int(row["priority"]), row["type"], row["details"]
                )
            )
            titles.append(row["title"].lower())
    print('Done! To see your list type "list"')


def remove():
    while True:
        removal = input("Input the title for removal: ")
        for i in range(len(todo_list)):
            if todo_list[i].title.lower().strip() == removal.lower().strip():
                todo_list.remove(todo_list[i])
                print(f'Removed {removal}. To see new list input "list"')
                return
        print("Invalid title")


def opening():
    print("Welcome to the To-Do List!")
    print('Type "help" for instructions or type "add" to add to your list.')


def help():
    print("help - lists all commands")
    print("add - adds to the list")
    print("list - displays your full to-do list")
    print("change - changes one parameter of an item in your list")
    print("remove - removes an item from your list")
    print("import - imports a fresh to do list from a .csv file")
    print("export - exports your list to a .csv file")
    print("exit - exits back to the main program")
    print("   be aware, list will not save unless you export to a file")


def list():
    if not todo_list:
        print("List is empty. Add items with \"add\"")
    else:
        # Sort list by priority 1 - 10
        sorted_list = []
        for i in range(1, 11):
            for item in todo_list:
                if item.priority == i:
                    sorted_list.append(item)
        # Print new list
        for item in sorted_list:
            print(item)


def exit():
    will_exit = (
        input(
            "Are you sure you want to exit? List will not be saved unless exported. (y/n) "
        )
        .lower()
        .strip()
    )
    if will_exit == "y":
        print("Thanks for using my To-Do List program!")
        project.project()


if __name__ == "__main__":
    todo()
