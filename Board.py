class Board:
    def __init__(self):
        board = [" "," "," ",
                " "," "," ",
                " "," "," "]
    def print_board(self):
        print(f"  {self.board[0]}| {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f"  {self.board[3]}| {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f"  {self.board[6]}| {self.board[7]} | {self.board[8]}")

    def update_board(self,position,type):
        try:
            if self.board[position - 1] == " ":
                self.board[position - 1] = type
                return True
            else:
                print("Position has already been selected. Enter a new position")
                return False
        except:
            print("Invalid position entered, please enter a position between (1-9) ")

    def check_winner(self,type):
        if self.board[0] == type and self.board[1] == type and self.board[2] == type or \
           self.board[3] == type and self.board[4] == type and self.board[5] == type or \
           self.board[6] == type and self.board[7] == type and self.board[8] == type or \
           self.board[0] == type and self.board[3] == type and self.board[6] == type or \
           self.board[1] == type and self.board[4] == type and self.board[7] == type or \
           self.board[2] == type and self.board[5] == type and self.board[8] == type or \
           self.board[0] == type and self.board[4] == type and self.board[8] == type or \
           self.board[2] == type and self.board[4] == type and self.board[6] == type:
            return True
        else:
            return False

    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False