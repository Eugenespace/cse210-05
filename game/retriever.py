'''
Retriever class 

To provide random word from word file.

get_word_set returns array in format = [[WORD BROKEN DOWN TO LETTERS], LETTER COUNT, BLANK UNDERSCORES TO REP WORD LETTERS]

'''
import csv
import random


class Retriever:

    def __init__(self):
        '''
        Set initial word list file name (csv format), lists and arrays via the constructor.
        '''
        self._file = "cse210-05/game/words_source.csv"
        self._total_words = ()
        self._letters = []
        self._letter_hider = []

    def get_word_list(self):
        '''
        Read CSV file and return list. Will return file error if file not found.
        '''
        try:
            with open(self._file) as words:
                word = csv.reader(words)

                for word in words:
                    stripped = word.strip()
                    self._total_words = stripped.split(",")

                # print(self._total_words)
                return self._total_words

        except FileNotFoundError as file_not_found:
            print(file_not_found)

    def get_word(self, list):
        '''
        Randomized word selection from word list. 
        Returns a randomly selected word.

        Argument "list": Enter custom list array,
                        Defaulted to use csv file
        '''
        _count = len(list)
        random_seed = random.randint(0, _count)
        # print(random_seed)
        chosen_word = self._total_words[random_seed]
        # print(chosen_word)
        return chosen_word

    def get_letters(self, a_word):
        '''
        Break up word into list of individual letters.
        Returns letter list in an array

        Argument "a_word": Enter custom word to be separated
                          Defaulted to get_word() return
        '''
        chosen_word = a_word

        for letter in chosen_word:
            self._letters.append(letter)

        return self._letters

    def get_letter_count(self, letter_array):
        '''
        Returns the number of letters from the given word.

        Argument "letter_array": Enter array of letters
                                Defaulted to get_letters() return
        '''
        letters = letter_array

        letter_count = len(letters)
        return letter_count

    def hidden_letters(self, letter_count):
        '''
        Takes given letter count and returns array of blanks (underscores)
        for each letter.

        Argument "letter_count": Enter number of blanks
                                Defaulted to letter_count return
        '''
        i = 0

        while i < letter_count:
            self._letter_hider.append("_")
            i += 1

        return self._letter_hider

    def get_word_set(self):
        '''
        Utilizes all modules to return the randomly chosen word broken 
        into each individual letter (array), the letter count, and the
        underscore blanks representing the letters (array).  
        '''
        words_array = []
        word_list = self.get_word_list()
        word = self.get_word(word_list)
        letters_array = self.get_letters(word)
        letter_count = self.get_letter_count(letters_array)
        hidden_letter = self.hidden_letters(letter_count)

        words_array.append(letters_array)
        words_array.append(letter_count)
        words_array.append(hidden_letter)

        return words_array


# --------------------- csv_retriever in practice ----------------
'''
## Instantiate Retriever
r = Retriever()

## set get_word_set to return array containing [0] revealed word, [1] letter count, [2] blanks for letters
custom_word = r.get_word_set()

## output 
print(custom_word)
'''
