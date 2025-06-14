class NumberFilter:
    def __init__(self):
        self.filtered_numbers = []

    def validate_if_odd(self):
        for number in range(100):
            if number % 5 != 0:
                self.filtered_numbers.append(number)

    def print_result(self):
        print("Odd numbers:", self.filtered_numbers)

filtered_numbers = NumberFilter()
filtered_numbers.validate_if_odd()
filtered_numbers.print_result()