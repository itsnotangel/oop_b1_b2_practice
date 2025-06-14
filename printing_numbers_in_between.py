class NumbersInBetween:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def show_numbers_in_between(self):
        if self.number_1 == self.number_2:
            print("Equal")
        elif abs(self.number_1 - self.number_2) == 1:
            print("Consecutive")
        else:
            start = min(self.number_1, self.number_2)
            end = max(self.number_1, self.number_2)
            for number in range(start + 1, end):
                print(number)

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
NumbersInBetween(number_1, number_2).show_numbers_in_between()