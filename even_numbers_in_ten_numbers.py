class EvenNumberSumCalculator:
    def __init__(self):
        self.numbers = []
        self.total_sum = 0

    def get_numbers(self):
        for number in range(10):
            user_input = int(input("Enter number: "))
            self.numbers.append(user_input)
            self.total_sum = sum(self.numbers)

    def print_result(self):
        print("Total of even numbers: ", self.total_sum)

calculator = EvenNumberSumCalculator()
calculator.get_numbers()
calculator.print_result()