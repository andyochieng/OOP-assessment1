class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

result1 = Calculator.add(1, 20)
print("Result 1:", result1)
print("Add method called:", Calculator.count, "times")

result2 = Calculator.add(15, 12)
print("Result 2:", result2)
print("Add method called:", Calculator.count, "times")
result3 = Calculator.add(9, 6)
print("Result 3:", result3)
print("Add method called:", Calculator.count, "times")