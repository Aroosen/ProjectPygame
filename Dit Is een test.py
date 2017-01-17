output = ""
User = int(input("Enter a number here"))
for y in range(User + 1):
    for x in range(User * 2 + 1):
        if x == User - y or x == User + y:
            output += "*"
        elif x >= User - y and x <= User + y:
            output += "*"
        else:
            output +=