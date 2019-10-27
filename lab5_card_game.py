# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 17-10-2019
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *
# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle

class CardGame(Frame):

    # initialises the application
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score

        self.player_score=0
        self.done = False

        self.create_deck()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        self.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(self)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(self)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)

        closed_deck = Button(cards_frame, command=self.draw_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.done_game)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.new_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Score: "+ str(self.player_score), justify=LEFT)
        self.score_label.pack()

        top_card = self.new_game()

        try:
            the_card = PhotoImage(file='cards/' + top_card + '.gif')
        #the_card = PhotoImage(file='cards/queen_hearts.gif')
        except:
            print('An error occured opening the image')
            self.game_exit()

        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    def create_deck(self):

        suits = ('hearts', 'diamonds', 'clubs', 'spades')
        faces = ('jack', 'queen', 'king')
        self.deck = []

        for i in range(1, 11):
            for suit in suits:
                self.deck.append(str(i) + '_' + suit)
        
        for suit in suits:
            for face in faces:
                self.deck.append(face + '_' + suit)

    def new_game(self):

        self.done = False
        self.player_score = 0

        self.cards = Queue(maxsize=52)

        shuffle(self.deck)

        for card in self.deck:
            self.cards.put(card)
        
        return self.draw_card()
    

    def draw_card(self):

        if self.done == False:

            self.top = self.cards.get()

            try:
                the_card = PhotoImage(file='cards/' + self.top + '.gif')
            except:
                print('An error occured opening the image')
                self.game_exit()

            self.open_card.config(image=the_card)
            self.open_card.grid(row=0, column=0, padx=2, pady=2)
            self.open_card.photo = the_card

            self.calculate_score(self.top)

            return self.top

    def calculate_score(self, card):

        self.card = card
        score = str(self.card).split('_')[0]

        if score.isdigit():
            self.player_score += int(score)
        else:
            self.player_score += 10

        self.check_score()

    def check_score(self):

        if self.player_score == 21:
            self.score_label.config(text='Score: ' + str(self.player_score) + '. Congrats you won!')
            self.done = True

        elif self.player_score > 21:
            self.score_label.config(text='Score: ' + str(self.player_score) + '. You lost!')
            self.done = True

        else:
            self.score_label.config(text='Score: ' + str(self.player_score))

        self.score_label.update_idletasks()

    def done_game(self):
        
        if self.done == False:
            self.done = True
            self.score_label.config(text='Score: ' + str(self.player_score) + '. Thanks for playing!')

# object creation here:
root = Tk()
root.geometry("300x200")
root.title("Card Game")
app = CardGame(root)
root.mainloop()
