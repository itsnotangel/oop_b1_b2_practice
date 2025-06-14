class NumberCalculator:
    def __init__(self):
        self.numbers = []
        self.total_sum = 0

    def get_numbers(self):
        for number in range(10):
            user_input = int(input("Enter a number: "))
            self.numbers.append(user_input)
            self.total_sum = sum(self.numbers)

    def print_result(self):
        print("Total sum of all ten numbers: ", self.total_sum)

calculator = NumberCalculator()
calculator.get_numbers()
calculator.print_result()