from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()
        self.current_player = self.player1

    def play(self):
        try:
            while True:
                message = f"{self.current_player.name}, Enter the position you wish to play in between (1-9): "
                position = int(input(message))
                while True:
                    if self.board.update_board(position,self.current_player.type) == True:
                        self.board.print_board()
                        break
                    else:
                        message = f"{self.current_player.name}, Enter the position you wish to play in between (1-9): "
                        position = int(input(message))

                if self.board.check_winner(self.current_player.type):
                    print(f"Congratulations {self.current_player.name}, You win the game ")
                    break
                elif self.board.check_draw():
                    print("Game is a draw")
                    break
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1

        except:
            print("Invalid argument entered!")

game = Game()
game.play()
