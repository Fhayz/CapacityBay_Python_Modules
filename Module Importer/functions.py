def display(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
