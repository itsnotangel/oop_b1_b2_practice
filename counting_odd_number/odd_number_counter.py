class OddNumberCounter:
    def __init__(self):
        self.number = []
        self.odd_count = 0

    def get_numbers(self):
        for i in range(10):
            user_input = int(input("Enter number: "))
            self.number.append(user_input)
            if user_input % 2 !=0:
                self.odd_count += 1

    def print_odd_count(self):
        print("Number of odd:", self.odd_count)