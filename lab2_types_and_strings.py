#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print(message[0] + message[-1])

        # use slice notation
        print(message[2:7:2])

        # escaping a character
        print("\nHe said that's fantastic")

        # find all a's in the input word and count how many there are
        print('\nLetter \'a\' appears at index: {}'.format(message.find('a')))
        print('Count of \'a\' is: {}'.format(message.count('a')))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        for i in range(0, len(message)):
            print(message[i].replace('a','-'))

        print('\n\n')
        # printing only characters at even index positions
        for i in range(0, len(message)):
            if i%2 == 0:
                print(message[i])

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        list_string = list(message)

        # append a new element to the list and print
        list_string.append('g')
        #print(list_string)

        # remove from the list in 3 ways
        list_string.remove('i')
        list_string.pop(2)
        del list_string[2]

        print(list_string)
        # check if the word cake is in your input list
        if 'man' in list_string:
            print('\nfound')

        # reverse the items in the list and print
        list_string[0], list_string[1] = list_string[1], list_string[0]
        print(list_string)

        # reverse the list with the slicing trick
        list_string[::-1]

        # print the list 3 times by using multiplication


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()