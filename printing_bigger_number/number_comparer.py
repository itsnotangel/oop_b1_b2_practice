class NumberComparer:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_numbers(self):
        self.num1 = float(input("Enter number 1: "))
        self.num2 = float(input("Enter number 2: "))

    def compare_numbers(self):
        if self.num1 > self.num2:
            print(self.num1, "is bigger.")
        elif self.num1 < self.num2:
            print(self.num2, "is bigger.")
        else:
            print("Equal numbers.")