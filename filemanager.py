def showContent():
    print("Content:")
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
showContent()