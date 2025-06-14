class NumberSubtractor:
    def __init__(self):
        self.numbers = []
        self.total_sum = 0

    def get_first_number(self):
        number_1 = int(input("Enter base number: "))
        self.total_sum = number_1

    def subtract_remaining_numbers(self):
        for number in range(9):
            user_input = int(input("Enter number: "))
            self.numbers.append(user_input)
            self.total_sum -= user_input

    def print_result(self):
        print("Total:", self.total_sum)

subtractor = NumberSubtractor()
subtractor.get_first_number()
subtractor.subtract_remaining_numbers()
subtractor.print_result()