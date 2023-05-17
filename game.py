from tkinter import *
from tkinter import messagebox

class ttt:
    def __init__(self):
        self.current_player = 'X'
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.root = Tk()
        self.root.title('ttt')
        self.create_labels()
        self.create_buttons()
        self.reset_button = Button(self.root, text='Reset', command=self.reset)
        self.reset_button.grid(row=6, column=1)

    def create_labels(self):
        self.player_label = Label(self.root, text=f"Current player: {self.current_player}")
        self.player_label.grid(row=0, column=0, columnspan=3)
        self.result_label = Label(self.root, text='')
        self.result_label.grid(row=1, column=0, columnspan=3)
    
    def create_buttons(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = Button(self.root, text=' ', width=10, height=5, command=lambda row=row, col=col: self.play(row, col))
                button.grid(row=row+2, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
    
    def play(self, row, col):

        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_win()
            if winner:
                self.buttons[row][col].config(bg='grey')
                self.show_message(f'{winner} wins!')
                self.reset()
            elif self.check_tie():
                self.buttons[row][col].config(bg='grey')
                self.show_message('Tie!')
                self.reset()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_label.config(text=f"Current player: {self.current_player}")
                self.buttons[row][col].config(bg='grey')
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return self.board[0][0]
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                return self.board[0][2]
        return None
    
    def check_tie(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True
    
    def show_message(self, message):
        messagebox.showinfo('Game Over', message)
    
    def reset(self):
        self.current_player = 'X'
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for row in self.buttons:
            for button in row:
                button.config(text=' ', bg='SystemButtonFace')
        self.player_label.config(text=f"Current player: {self.current_player}")
        self.result_label.config(text='')

    def highlight_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.buttons[i][0].config(bg='green')

    def play_game(self):
        self.root.mainloop()

game = ttt()
game.play_game()
