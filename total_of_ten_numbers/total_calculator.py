class TotalOfTenNumberCalculator:
    def __init__(self):
        self.numbers = []
        self.total = 0.0

    def get_numbers(self):
        for i in range(10):
            user_input = float(input("Enter number: "))
            self.numbers.append(user_input)
        self.total = sum(self.numbers)

    def print_total(self):
        print("Total of the numbers:", self.total)