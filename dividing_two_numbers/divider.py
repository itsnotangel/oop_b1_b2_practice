class NumberDivider:
    def __init__(self):
        self.number_1 = 0
        self.number_2 = 0

    def get_numbers(self):
        self.number_1 = float(input("Enter number 1: "))
        self.number_2 = float(input("Enter number 2: "))

    def divide_numbers(self):
        if self.number_2 == 0:
            print("Indeterminate.")
        else:
            quotient = self.number_1 / self.number_2
            print("Result:", quotient)