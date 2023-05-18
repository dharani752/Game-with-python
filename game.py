class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # Initialize an empty board
        self.current_player = 'X'  # 'X' starts the game

    def display_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print("|", self.board[i], "|", self.board[i + 1], "|", self.board[i + 2], "|")
            print("-------------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combination in winning_combinations:
            a, b, c = combination
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]

        if ' ' not in self.board:
            return 'Draw'

        return None

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Here is the board:")
        self.display_board()

        while True:
            print(f"\nPlayer {self.current_player}'s turn.")
            position = int(input("Enter a position (0-8): "))

            self.make_move(position)
            self.display_board()

            winner = self.check_winner()
            if winner:
                if winner == 'Draw':
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                break


# Run the game
game = TicTacToe()
game.play()
