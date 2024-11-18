class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        for _ in range(b): 
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = 0
        while a >= b: 
            a = self.subtract(b, a)
            result += 1
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        while a >= b:  
            a = self.subtract(a, b)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))