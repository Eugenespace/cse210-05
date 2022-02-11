class Jumper:
    """Takes care of the Parachute. 
    Attribute:jumper parachute
    """

    def __init__(self):
        """Constructs jumper parachute"""
        # self._jumperParachute = [" _____", "/_____\\",
        #                          "\\     /", " \\   /", "   0 ", "  /|\\", "  / \\"]
        j1 = (f"\n   _____  ")
        j2 = (f"  /_____\ ")
        j3 = (f"  \     /")
        j4 = (f"   \   / ")
        j5 = (f"     O   ")
        j6 = (f"    /|\  ")
        j7 = (f"    / \  ")
        j8 = (f"\n^ ^ ^ ^ ^ ^ ^")
        self._jumperParachute = [j1, j2, j3, j4, j5, j6, j7, j8]
        for i in range(len(self._jumperParachute)):
            print(self._jumperParachute[i])

    def get_parachute(self):
        """creates a parachute array"""
        # return self._jumperParachute

    def untie_parachute(self, guess):
        """If guess is right the parachute remains intact if not untie the parachute"""
        if guess:
            self._jumperParachute = self._jumperParachute
        else:
            self._jumperParachute.pop(0)
        return self._jumperParachute

    def fallen_jumper(self):
        """if all parachute is untied, set falling to False"""
        falling = True

        if (len(self._jumperParachute) == 3):
            self._jumperParachute[0] = " X "
            falling = False

        return falling


# class Jumper_guy:
#     def __init__(self):
#         self.player_guess


# #Testing the jumper display:
#     def player_guess(self, guess):
#         '''
#         --------Testing-------------
#         correct = "a"
#         incorrect = "z"

#         guess = input("choose a letter: ")'''


#         j1 = (f"\n _____  ")
#         j2 = (f"  /_____\ ")
#         j3 = (f"  \     /")
#         j4 = (f"   \   / ")
#         j5 = (f"     O   ")
#         j6 = (f"    /|\  ")
#         j7 = (f"    / \  ")
#         j8 = (f"\n^ ^ ^ ^ ^ ^ ^")

#         jX = (f"\n     X   ")
#         jOver = (f"\nGame Over!\n")

#         jumper = [j1, j2, j3, j4, j5, j6, j7, j8]
#         jumperGameOver = [jX, j6, j7, j8, jOver]

#         if guess == correct:
#             for i in range(len(jumper)):
#                 print (jumper [i])

#         else:
#             if guess == incorrect:
#                 jumper.pop(1)
#                 for i in range(len(jumper)):
#                     print (jumper [i])

#             else:
#                 for i in range(len(jumperGameOver)):
#                     print (jumperGameOver[i])
