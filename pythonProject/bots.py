import random

def random_bot(_):
    return random.choice(["R", "P", "S"])

def repetitive_bot(_):
    return "R"

def pattern_bot(prev_play):
    sequence = ["R", "P", "S"]

    if not prev_play:
        return "R"
    return sequence[(sequence.index(prev_play) + 1) % 3]

def counter_bot(prev_play):
    """counters players last move"""
    counters = {"R": "P", "P": "S", "S": "R"}
    if not prev_play:
        return "R"
    return counters[prev_play]


def adaptive_play(prev_play, player_history=[]):
    """adapts to the player's last two moves to predict the next"""
    if not prev_play:
        player_history.clear()

    player_history.append(prev_play)

    if len(prev_play) < 3:
        return random.choice(["R", "P", "S"])

    recent_pattern = "".join(player_history[-2:])
    patterns =  {"RR": "P", "RP": "S", "RS": "R",
                "PP": "S", "PS": "R", "PR": "P",
                "SS": "R", "SR": "P", "SP": "S"}

    return patterns.get(recent_pattern, random.choice(["R", "P", "S"]))