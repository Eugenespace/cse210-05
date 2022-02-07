
class Jumper_guy:
    def __init__(self):
        self.player_guess 


#Testing the jumper display:
    def player_guess(self, guess):
        correct = "a"
        incorrect = "z"

        guess = input("choose a letter: ")


        j1 = (f"\n _____  ")
        j2 = (f"  /_____\ ")
        j3 = (f"  \     /")
        j4 = (f"   \   / ")
        j5 = (f"     O   ")
        j6 = (f"    /|\  ")
        j7 = (f"    / \  ")
        j8 = (f"\n^ ^ ^ ^ ^ ^ ^")

        jX = (f"\n     X   ")
        jOver = (f"\nGame Over!\n")

        jumper = [j1, j2, j3, j4, j5, j6, j7, j8]
        jumperGameOver = [jX, j6, j7, j8, jOver]

        if guess == correct:
            for i in range(len(jumper)):
                print (jumper [i])

        else:
            if guess == incorrect:
                jumper.pop(1)
                for i in range(len(jumper)):
                    print (jumper [i])

            else:
                for i in range(len(jumperGameOver)):
                    print (jumperGameOver[i])



