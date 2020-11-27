import numpy as np
# change to dropping the move in one column rather than choose the coordinate.

class Game():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = np.zeros((row,col))
        self.state = 1
    
    def get_grid(self):
        return self.grid
    
    def get_state(self):
        return self.state

    def play(self):
        user_input = input("Where would you like to play your turn? : ")
        r = int(user_input[0]) - 1
        c = int(user_input[1]) - 1
        assert r >= 0 and r <= 5
        assert c >= 0 and c <= 6 
        if self.grid[r,c] != 0:
            print("not zero")
            print("Invalid move")
        elif r+1 != self.row:
            if self.grid[r+1,c] == 0:
                print("below empty")
                print("Invalid move")
            else:
                user_colour = int(input("1 or 2? : "))
                self.grid[r,c] = user_colour
        else:
            user_colour = int(input("1 or 2? : "))
            self.grid[r,c] = user_colour

        return self.get_grid()

    def __connections(self):
        neighbours = {}



