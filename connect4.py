import numpy as np

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
        user_input = input("Which column do you choose ? : ")
        c = int(user_input) - 1
        assert c >= 0 and c <= self.col
        if self.grid[0,c] != 0:
            print("Choose another column.")
            self.play()
        else:
            user_colour = int(input("1 or 2? : "))
            for i in range(self.row-1):
                if self.grid[i+1,c] != 0:
                    self.grid[i,c] = user_colour
                else:
                    self.grid[self.row,c] = user_colour

        return self.get_grid()

    def __connections(self):
        neighbours = {}



