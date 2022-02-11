from retriever import Retriever
from jumper_guy import Jumper
from word_handler import Word_handler


class Director:

    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper_guy (Jumper_guy): The game's player guess.
        retriever(Retriever) : Retrieves words from a list.

        """
    #retriever = Retriever()

    def __init__(self):
        self.isPlaying = True
        self.jumper_guy = Jumper()
        retriever = Retriever()
        self.handler = Word_handler()

        self.word_set = retriever.get_word_set()

        self.chosen_word = self.word_set[0]
        self.letter_count = self.word_set[1]
        self.blanks = self.word_set[2]

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        while self.isPlaying:
            self._do_intro()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _do_intro(self):
        # self.jumper_guy.player_guess(guess)
        ''' ----------Possible outputs----------
        blanks = .guess_true'''
        print(self.chosen_word)
        print(self.blanks)
        print()
        pass

    def _get_inputs(self):
        """Gets player guess (letter in the puzzle).

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input("choose a letter: ")
        return self.guess

    def _do_updates(self):
        """Keeps watch on what letter the player will guess.

        Args:
            self (Director): An instance of Director.
        """
        # this is where the handler will check the letter against array and update blanks
        self.valid_guess = Word_handler.guess_check(
            self.guess, self.letter_count, self.chosen_word)
        self.blanks = Word_handler.guess_true(
            self.guess, self.chosen_word, self.blanks)
        print(self.blanks)
        if self.valid_guess == True:
            # Do the true stuff
            # the blank updated update jumper

            print("Nailed it")
        elif self.valid_guess == False:
            # do the false stuff
            # update jumper and blanks
            print("WRONG!")

        # if chosen_letter
        # return blanks array

    def _do_outputs(self):
        print("Output here")
