#Defines the advanced player using a Markov chain

from collections import defaultdict
import random

def markov_chain_player(prev_play, opponent_history=[]):
    """
    An adaptive player using a Markov chain to predict the opponent's next move.
    """

    if not prev_play:
        opponent_history.clear()

    opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Build Markov chain from the history
    transition_counts = defaultdict(lambda: {"R":0, "P":0, "S":0})
    for i in range(len(opponent_history) - 1):
        current_move = opponent_history[i]
        next_move = opponent_history[i + 1]
        transition_counts[current_move][next_move] += 1

    last_move = opponent_history[-1]
    if sum(transition_counts[last_move].values()) == 0:
        predicted_next_move = random.choice(["R", "P", "S"])
    else:
        predicted_next_move = max(transition_counts[last_move], key=transition_counts[last_move].get)

    counters = {"R": "P", "P": "S", "S": "R"}
    return counters[predicted_next_move]
