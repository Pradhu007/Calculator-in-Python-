class Calculator:


    def __init__(self,number1,number2):
        self.number1= number1
        self.number2 = number2

    def add(self):
        return  self.number1 + self.number2

    def subract(self):
        return self.number1-self.number2


    def divide(self):
        return self.number1-self.number2

    def multiply(self):
        return self.number1*self.number2


def options():
    print("1. Add ")
    print("2.Subract")
    print("3. Multiply")
    print("4. Divide ")

while True:

    num1 = int(input("What is your first number?"))
    num2 = int(input("What is your second number?"))

    Calculate = Calculator(num1, num2)


    options()
    op = input(">")
    if op == "1":
      op = "+"
      print("The result of  ",num1,op, num2 , "=", Calculate.add())

    elif op == "2":
        op = "-"
        print("The result of  ", num1, op, num2, "=", Calculate.subract())


    elif op == "3":
        op = "x"
        print("The result of  ", num1, op, num2, "=", Calculate.multiply())

    elif op == "4":
        op = "/"
        print("The result of  ", num1, op, num2, "=", Calculate.divide())
    else:
        break





















