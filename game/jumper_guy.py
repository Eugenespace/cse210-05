class Jumper:
    """Takes care of the Parachute.
    Attribute:jumper parachute
    """

    def __init__(self):
        """Constructs jumper parachute"""
        # This variable is private (__)
        self.__num = 0

        j1 = (f"\n   _____  ")
        j2 = (f"  /_____\ ")
        j3 = (f"  \     /")
        j4 = (f"   \   / ")
        j5 = (f"     O   ")
        j6 = (f"    /|\  ")
        j7 = (f"    / \  ")
        j8 = (f"\n^ ^ ^ ^ ^ ^ ^")
        # This variable is protected (_)
        self._jumperParachute = [j1, j2, j3, j4, j5, j6, j7, j8]

        jX = (f"\n     X   ")
        jOver = (f"\nGame Over!\n")
        self.jumperGameOver = [jX, j6, j7, j8, jOver]

        for i in range(len(self._jumperParachute)):
            print(self._jumperParachute[i])

    def get_parachute(self):
        """default jumper guy parachute array"""

    def untie_parachute(self):
        # If guess is right the parachute remains intact if not untie the parachute
        for i in range(len(self._jumperParachute)):
            print(self._jumperParachute[i])

    def fallen_jumper(self):
        """if all parachute is untied, set falling to False"""
        self._jumperParachute.pop(self.__num)
        for i in range(len(self._jumperParachute)):
            print(self._jumperParachute[i])
