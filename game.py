# Import necessary libraries
import numpy as np
import random

# Define Connect 4 game environment
class Connect4Environment:
    def __init__(self):
        self.board = np.zeros((6, 7))  # 6x7 game board
        self.current_player = 1  # Player 1 starts
        self.winner = None
        self.game_over = False

    def reset(self):
        self.board = np.zeros((6, 7))
        self.current_player = 1
        self.winner = None
        self.game_over = False

    def is_valid_move(self, column):
        return self.board[0][column] == 0

    def make_move(self, column):
        if not self.is_valid_move(column):
            return False
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                break
        self.current_player = 3 - self.current_player  # Switch player
        return True

    def check_winner(self):
        # Implement your win-checking logic here
        # Return 1 for Player 1 win, 2 for Player 2 win, 0 for no winner, -1 for draw
        pass

    def is_game_over(self):
        # Check for a winner or a draw
        self.winner = self.check_winner()
        if self.winner is not None:
            self.game_over = True
        elif np.all(self.board != 0):
            self.winner = -1  # Draw
            self.game_over = True
        return self.game_over

    def get_state(self):
        # Return the current state of the board
        return self.board.copy()

    def get_valid_moves(self):
        # Return a list of valid moves (columns)
        valid_moves = []
        for column in range(7):
            if self.is_valid_move(column):
                valid_moves.append(column)
        return valid_moves

# Define a simple random agent for testing
class RandomAgent:
    def __init__(self, player):
        self.player = player

    def choose_move(self, valid_moves):
        return random.choice(valid_moves)

# Main training loop
def train_connect4_agent():
    # Initialize Connect 4 environment and agents
    env = Connect4Environment()
    player1_agent = RandomAgent(1)
    player2_agent = RandomAgent(2)

    num_episodes = 10000  # Adjust as needed

    for episode in range(num_episodes):
        env.reset()
        while not env.is_game_over():
            if env.current_player == 1:
                move = player1_agent.choose_move(env.get_valid_moves())
            else:
                move = player2_agent.choose_move(env.get_valid_moves())
            env.make_move(move)

        # Update agent policies/values here (RL training)

    # Save trained model parameters if needed

if __name__ == "__main__":
    train_connect4_agent()
# ... (previous code)

# Define a human player agent
class HumanPlayer:
    def __init__(self, player):
        self.player = player

    def choose_move(self, valid_moves):
        while True:
            try:
                move = int(input("Player {}, choose a column (0-6): ".format(self.player)))
                if move in valid_moves:
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 0 and 6.")

# Main gameplay loop
def play_connect4_game():
    env = Connect4Environment()
    player1_agent = RandomAgent(1)  # Replace with your RL agent
    player2_agent = HumanPlayer(2)  # Human player

    while True:
        env.reset()
        while not env.is_game_over():
            if env.current_player == 1:
                move = player1_agent.choose_move(env.get_valid_moves())
            else:
                move = player2_agent.choose_move(env.get_valid_moves())
            env.make_move(move)
            print(env.get_state())  # Display the game board

        # Determine the winner and display the result
        if env.winner == -1:
            print("It's a draw!")
        else:
            print("Player {} wins!".format(env.winner))


        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_connect4_game()