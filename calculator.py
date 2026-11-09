class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0

        if b >= 0:
            for _ in range(b):
                result = self.add(result, a)
        else:
            for _ in range(-b):
                result = self.subtract(result, a)

        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        negative = (a < 0) != (b < 0)

        if a < 0:
            a = self.subtract(0, a)
        if b < 0:
            b = self.subtract(0, b)

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if negative:
            result = self.subtract(0, result)

        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")

        if a < 0 or b < 0:
            raise ValueError("Modulo supports non-negative integers only")

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