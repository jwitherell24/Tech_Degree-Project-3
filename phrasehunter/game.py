from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("In a year that has been so improbable the impossible has happened"),
                        Phrase("Behind the bag it gets through Buckner"),
                        Phrase("The Giants win the pennant"),
                        Phrase("Go crazy folks go crazy"),
                        Phrase("Juuust a bit outside")
                       ]
        self.active_phrase = None
        self.guesses = [" "]

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase

    def welcome(self):
        print(
        """====================================
Welcome to Phrase Hunter!
====================================\n
The hidden phrases are some famous baseball calls from throughout history (and one from the movies).
You have 5 chances to guess it correctly!"""
        )

    def start(self):
        self.welcome()
        self.get_random_phrase()

        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nIncorrect guesses: {self.missed}")
            self.active_phrase.display(self.guesses)

            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)

            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1

        self.game_over()

    def get_guess(self):
        user_input = input("\n\nPlease guess a letter from A-Z.  ").lower()

        while True:
            if user_input.lower() < "a":
                user_input = input("Sorry, that is not a valid guess, please guess again from A-Z.  ")
                continue

            if user_input.lower() > "z":
                user_input = input("Sorry, that is not a valid guess, please guess again from A-Z.  ")
                continue

            if len(user_input) != 1:
                user_input = input("Sorry, that is not a valid guess, please guess again from A-Z.  ")
                continue

            else:
                return user_input

    def game_over(self):
        if self.missed == 5:
            print("Sorry, you have lost the game!")
            self.play_again()

        else:
            self.active_phrase.display(self.guesses)
            print("\n\nCongratulations! You've won the game!\n")
            self.play_again()

    def play_again(self):
        play_again = input("Would you like to play again? (Enter Y/y to start over, any other key to quit)  ")
        if play_again.lower() == "y":
            self.missed = 0
            self.active_phrase = self.get_random_phrase()
            self.guesses = [" "]
            self.start()
        else:
            print("Thanks for playing!")
