def calculate(x, oper, y):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/":
        return x / y


def lazy(x, oper, y):
    msg = ""
    if (x % 1 == 0 and y % 1 == 0) and (x < 10 and y < 10):
        msg += " ... lazy"
    if x == 1 or y == 1 and oper == "*":
        msg += " ... very lazy"
    if (x == 0 or y == 0) and (oper == "+" or oper == "-" or oper == "*"):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
    return msg


M = "0"
while True:
    x, oper, y = input("Enter an equation\n").split()
    if x == "M":
        x = M
    if y == "M":
        y = M
    if x.isalpha() or y.isalpha():
        print("Do you even know what numbers are? Stay focused!")
    elif oper not in ["+", "-", "/", "*"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    elif oper == "/" and y == "0":
        x, y = float(x), float(y)
        print(lazy(x, oper, y))
        print("Yeah... division by zero. Smart move...")
    else:
        x, y = float(x), float(y)
        print(lazy(x, oper, y))
        answer = (calculate(x, oper, y))
        print(answer)
        if input("Do you want to store the result? (y / n):\n") == "y":
            if answer < 10 and answer % 1 == 0:
                why = input("Are you sure? It is only one digit! (y / n)\n")
                if why == "y":
                    why = input("Don't be silly! It's just one number! Add to the memory? (y / n)\n")
                    if why == "y":
                        why = input("Last chance! Do you really want to embarrass yourself? (y / n)\n")
                        if why == "y":
                            M = str(answer)
            else:
                M = str(answer)
        if input("Do you want to continue calculations? (y / n):\n") == "n":
            break

