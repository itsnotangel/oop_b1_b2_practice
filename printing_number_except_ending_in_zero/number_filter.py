class NumberFilter:
    def printing_number_except_ending_in_zero(self):
        for number in range(1, 100):
            if number % 10 !=0:
                print(number)