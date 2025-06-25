import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.x_score = 0
        self.o_score = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        self.status_label = tk.Label(text=f"Player {self.current_player}'s turn", font=('Arial', 14))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=5)

        self.score_label = tk.Label(text=self.get_score_text(), font=('Arial', 12))
        self.score_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.reset_button = tk.Button(text="Reset Board", font=('Arial', 12), command=self.reset_game)
        self.reset_button.grid(row=5, column=0, columnspan=3, pady=5)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                command=lambda r=row, c=col: self.make_move(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def get_score_text(self):
        return f"Score - X: {self.x_score} | O: {self.o_score}"

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.x_score += 1
                else:
                    self.o_score += 1
                self.score_label.config(text=self.get_score_text())
                return
            elif self.is_full():
                self.status_label.config(text="It's a tie!")
                messagebox.showinfo("Game Over", "It's a tie!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return True
            if b[0][i] == b[1][i] == b[2][i] != "":
                return True
        if b[0][0] == b[1][1] == b[2][2] != "" or b[0][2] == b[1][1] == b[2][0] != "":
            return True
        return False

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="")
        self.current_player = "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
