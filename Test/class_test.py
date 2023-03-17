def add():
    print("Add function")


def subtract():
    print("Subtract function")


def multiply():
    print("Multiply function")


def divide():
    print("Divide function")


commands = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

while True:
    user_input = input("Enter command: ")
    if user_input.lower() == "quit":
        break
    elif user_input in commands:
        commands[user_input]()
    else:
        print("Invalid command!")
