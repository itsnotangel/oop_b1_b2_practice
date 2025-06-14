class EvenNumberPrinter:
    def __init__(self):
        self.filtered_numbers = []

    def get_numbers(self):
        for number in range(2, 100, 2):
            if number % 2 == 0:
                self.filtered_numbers.append(number)

    def print_result(self):
        print("Even numbers:", self.filtered_numbers)

number_printer = EvenNumberPrinter()
number_printer.get_numbers()
number_printer.print_result()