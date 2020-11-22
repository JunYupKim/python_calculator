# calculator.py

class Calculator:
    def setData(self,number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):

        return self.number1 + self.number2

    def subtract(self):
        return self.number1 -self.number2

    def divide(self):
        if self.number2 is 0:
            return "Error: Numbers cannot be divided by 0"
        else:
            return self.number1 / self.number2

    def __init__(self):
        print "Calculation Completed!"