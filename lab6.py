class HappyNumbers:
    
    def __init__(self):
        number = int(input('Please enter a number: '))
        self.display(number)

    def calculation(self, number):

        single_digits = []
        sum = 0

        single_digits = [int(num) for num in str(number)]

        for i in range(0, len(single_digits)):
            sum = sum + single_digits[i] ** 2

        return sum

    def check(self, number):
        
        happy = number

        while happy != 4 and happy != 1:
            happy = self.calculation(happy)
        
        if happy == 1:
            print(number)

    def display(self, number):
        last = number + 1

        for i in range(1, last):
            self.check(i)

happy = HappyNumbers()   