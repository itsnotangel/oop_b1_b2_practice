class NumberFilter:
    def __init__(self):
        self.numbers = []
        self.odd_counter = 0

    def get_numbers(self):
        for number in range(10):
            user_input = int(input("Enter a number: "))
            self.numbers.append(user_input)
            if user_input % 2 != 0:
                odd_counter += 1

    def print_result(self):
        print ("Total of odd:", self.odd_counter)

number_filter = NumberFilter()
number_filter.get_numbers()
number_filter.print_result()