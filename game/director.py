from retriever import Retriever

class Director:
    def __init__(self):
        self.isPlaying = True
    def game_start(self):
        print("Jumper collaboration")

        r = Retriever()
        word_set = r.get_word_set()
        print(f"\n\nThe array from .get_word_set is: {word_set}\n\n")
        print(f"word_set[0] is the randomly chosen word broken into it's letters: {word_set[0]}\n")
        print(f"word_set[1] is the letter count: {word_set[1]}\n")
        print(f"word_set[2] is the letter blanks: {word_set[2]}\n")