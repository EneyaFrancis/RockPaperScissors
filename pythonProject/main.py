# The main entry point for running simulations and displaying results

from  simulate import  play_game
from bots import random_bot, repetitive_bot, pattern_bot, counter_bot, adaptive_bot
from adaptive_player import markov_chain_player

def main():
    num_games = 1000
    bots = {
        "Random Bot": random_bot,
        "Repetitive Bot": repetitive_bot,
        "Pattern Bot": pattern_bot,
        "Counter Bot": counter_bot,
        "Adaptive Bot": adaptive_bot
    }
    print("Rock, Paper, Scissors Tournament!\n")
    for bot_name, bot_function in bots.items():
        print(f"Playing against {bot_name}...")
        stats = play_game(markov_chain_player, bot_function, num_games)
        win_rate = (stats["player1_score"] / num_games) * 100

        print(f"Results against {bot_name}:")
        print(f"  Player 1 Wins: {stats['player1_score']}")
        print(f"  Player 2 Wins: {stats['player2_score']}")
        print(f"  Draws: {stats['draws']}")
        print(f"  Win Rate: {win_rate:.2f}%")
        print(f"  Player 1 Moves: {stats['player1_moves']}")
        print(f"  Player 2 Moves: {stats['player2_moves']}\n")


if __name__ == "__main__":
    main()