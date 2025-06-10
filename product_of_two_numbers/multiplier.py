class NumberMultiplier:
    def __init__(self):
        self.number_1 = 0
        self.number_2 = 0

    def get_numbers(self):
        self.number_1 = float(input("Enter number 1: "))
        self.number_2 = float(input("Enter number 2: "))

    def multiply_numbers(self):
        product = self.number_1 * self.number_2 
        print("Product:", product)