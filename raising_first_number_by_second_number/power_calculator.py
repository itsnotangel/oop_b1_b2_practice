class PowerCalculator:
    def __init__(self):
        self.number_1 = 0
        self.number_2 = 0

    def get_numbers(self):
        self.number_1 = int(input("Enter number 1: "))
        self.number_2 = int(input("Enter number 2: "))
    
    def raise_first_number_to_second(self):
        power = self.number_1 ** self.number_2
        print("Result:", power)