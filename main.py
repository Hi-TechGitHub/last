class Calculator:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def multiplication(self, x, y):
        return int(x * y)
    def summation(self, x, y):
        return int(x + y)
    def subtraction(self, x, y):
        return int(x - y)
    def division(self, x, y):
        return int(x / y)
x = int(input("Enter a x: "))
y = int(input("Enter an y: "))

math_operations = Calculator(x, y)
agree = str(input(f'you wanna {x} + {y}? yes or skip '))
if agree == "yes":
    print(math_operations.summation(x, y))
agree = str(input(f'you wanna {x} - {y}? yes or skip '))
if agree == "yes":
    print(math_operations.subtraction(x, y))
agree = str(input(f'you wanna {x} * {y}? yes or skip '))
if agree == "yes":
    print(math_operations.multiplication(x, y))
agree = str(input(f'you wanna {x} / {y}? yes or skip '))
if agree == "yes":
    print(math_operations.division(x, y))
