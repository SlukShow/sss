class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_win(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонталі
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикалі
            (0, 4, 8), (2, 4, 6)              # Діагоналі
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def start_game(self):
        while True:
            self.print_board()
            position = int(input(f"Гравець {self.current_player}, виберіть позицію (0-8): "))
            if 0 <= position < 9 and self.make_move(position):
                if self.check_win():
                    self.print_board()
                    print(f"Гравець {self.current_player} виграв!")
                    break
                if self.check_draw():
                    self.print_board()
                    print("Нічия!")
                    break
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Некоректний хід, спробуйте ще раз.")
