class NumberFilter:
    def __init__(self):
        self.filtered_numbers = []

    def validate_numbers(self):
        for number in range(100):
            if number % 10 != 0:
                self.filtered_numbers.append(number)

    def print_result(self):
        print("Numbers except ending in 0:", self.filtered_numbers)

number_filter = NumberFilter()
number_filter.validate_numbers()
number_filter.print_result()