# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        words = list(self.user_input)
        words[0], words[1] = words[1], words[0]
        words[-1], words[-2] = words[-2], words[-1]

        w = ''.join(words)

        print(w)
        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

        #welcome to my house

        for i in range(0, len(words), 3):
            if i < len(words) - 2:
                print(i)
                words[i], words[i+1] = words[i+1], words[i]

        print (words)

word_scrambler = WordScramble()
word_scrambler.scramble()

