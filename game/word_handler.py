
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
        '''EXAMPLE -
        for i in range (len(text_list)):
        if text_list [i] == 'AB':
            print (text_list [i])
            text_list [i] = "Alberta"
        count = text_list.count ("Alberta")

        print (text_list)
        Wayback Machine
        '''
        for i in range(len(chosenword)):
            if chosenword[i] == guess:
                blanks[i] = guess

        return blanks

        ''' 
        
        print(guess+"1")
        for guess in range(len(chosenword)):
            print(guess+"2")
            if chosenword[guess] == guess:
                print(guess+"3")
                #blanks[i] = guess
                

        
        return guess
        

    def guess_false():
        #
        pass
'''
