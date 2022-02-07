
from game.retriever import Retriever
from game.jumper_guy import Jumper_guy

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper_guy (Jumper_guy): The game's player guess.
        retriever(Retriever) : Retrieves words from a list.
        
        """

    def __init__(self):
        self.isPlaying = True
        self.jumper_guy = Jumper_guy
        self.retriever = Retriever
    
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def _get_inputs(self):
        """Gets player guess (letter in the puzzle).

        Args:
            self (Director): An instance of Director.
        """
        guess = input("choose a letter: ")
        self.jumper_guy.player_guess(guess)
        
    def _do_updates(self):
        """Keeps watch on what letter the player will guess.

        Args:
            self (Director): An instance of Director.
        """

  
        
    def _do_outputs(self):
      
    
    
    # def game_start(self):
    #     print("Jumper collaboration")

    #     r = Retriever()
    #     word_set = r.get_word_set()
    #     print(f"\n\nThe array from .get_word_set is: {word_set}\n\n")
    #     print(f"word_set[0] is the randomly chosen word broken into it's letters: {word_set[0]}\n")
    #     print(f"word_set[1] is the letter count: {word_set[1]}\n")
    #     print(f"word_set[2] is the letter blanks: {word_set[2]}\n")