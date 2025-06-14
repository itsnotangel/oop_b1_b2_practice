class OddPrinter:
    def __init__(self):
        self.filtered_numbers = []

    def validate_odd(self):
        number = 1
        while number < 100:
            self.filtered_numbers.append(number)
            number += 2

    def print_result(self):
        print("Odd number list:", self.filtered_numbers)

number_printer = OddPrinter()
number_printer.validate_odd()
number_printer.print_result()