print("*" * 10, "Калькулятор v 1.0", "*" * 10)
def main(calculator):
    s = input("Знак (+, -, *, /): ")
    if s == 'q': 'break'
    if s in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if s == "+":
            print("%d" % (x + y))
        elif s == "-":
            print("%d" % (x - y))
        elif s == "*":
            print("%d" % (x * y))
        elif s == "/":
            if y != 0:
                print("%d" % (x / y))
            else:
                print("Вы делите на ноль!")
    else:
        print("Неверный знак!")