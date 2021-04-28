import random

class Player:
    def __init__(self, marker='X', is_human=True):
        self._marker = marker
        self._is_human = is_human

    @property                   # can use name 'marker' outside of the class
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    # define 3 methods
    def get_player_move(self):
        # first check if the player is human or a computer
        if self._is_human:
            return self.get_human_move()
        # if not human, than call the get computer method
        else:
            return self.get_computer_move()

    def get_human_move(self):
        # this method asks for user input
        # store the input as a string in the variable 'move'
        move = input("Player move (X): ")
        return move

    def get_computer_move(self):
        # need to generate the row and the column randomly
        # use the 'import random' at the very top of the program
        # random.choice chooses an element randomly from a sequence. The sequence will be written by the programmer
        # since there are 3 rows, the sequence inside the brackets will be 1, 2, 3
        row = random.choice([1 , 2, 3])

        # since there are 3 columns that are labeled a,b,c this is how they will be referenced
        col = random.choice(["A", "B", "C"])

        move = str(row) + col)

        # now display the computer move so the player can see the latest computer move on the board
        # the (O) is to remind the payer that the computer's marker is O
        # then, str(row) is to convert the row numbers (1,2,3) into a string
        # the str(row) + col, will print ex: 1B (concatenation)
        print("Computer move (O): ", str(row) + col)

        return str(row) + col





