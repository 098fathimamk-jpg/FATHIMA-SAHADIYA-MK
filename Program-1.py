# Program-1.py
# Language: Python 3
# Small Calculator: performs addition, subtraction, multiplication, division

class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Unknown operation"

# Example usage below allows user input
if __name__ == "__main__":
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add/subtract/multiply/divide): ")
    calc = Calculator(a, b, operation)
    print("Result:", calc.calculate())
