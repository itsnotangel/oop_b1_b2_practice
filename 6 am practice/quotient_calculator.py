class QuotientCalculator:
    def __init__(self):
        self.number_1 = 0
        self.number_2 = 0

    def get_numbers(self):
        self.number_1 = int(input("Enter a number: "))
        self.number_2 = int(input("Enter a number: "))

    def calculate_quotient(self):
        if self.number_2 == 0:
            print("Cannot divide")
        else:
            self.quotient = self.number_1 / self.number_2
    
    def print_result(self):
        print("Quotient:", self.quotient)

calculator = QuotientCalculator()
calculator.get_numbers()
calculator.calculate_quotient()
calculator.print_result()