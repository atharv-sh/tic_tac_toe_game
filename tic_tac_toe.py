import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.winner = None

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", width=10, height=5,
                                  command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, column=0, columnspan=3)

        self.root.mainloop()

    def on_button_click(self, row, col):
        if self.board[row][col] == " " and not self.winner:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win():
                self.winner = self.current_player
                self.show_winner()
            elif self.check_draw():
                self.winner = "Draw"
                self.show_winner()
            else:
                self.switch_player()

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return True

        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != " ":
            return True

        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def show_winner(self):
        result_message = f"{'Player ' + self.winner} wins!" if self.winner != "Draw" else "It's a Draw!"
        tk.messagebox.showinfo("Game Over", result_message)

    def new_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.winner = None
        for row in self.buttons:
            for button in row:
                button.config(text=" ")

if __name__ == "__main__":
    game = TicTacToe()