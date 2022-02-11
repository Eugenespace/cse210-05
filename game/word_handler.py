
class Word_handler:
    def __init__(self):
        pass

    def guess_check(guess, count, chosenword):
        # check against the array - return true or false
        correct = False

        i = -1
        while i <= count:
            i = i + 1
            for letter in chosenword:
                if letter == guess:
                    correct = True

        return correct

    def guess_true(guess, chosenword, blanks):
        # parse the array and change the blank to corresponding letter location
        # return updated blank array

        for i in range(len(chosenword)):
            if chosenword[i] == guess:
                blanks[i] = guess

        return blanks

    def guess_false():
        #
        pass
