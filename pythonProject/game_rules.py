# this module contains the core rules for the game

#game rules
def decide_winner(player_move, opponent_move):
    """
    Determine the winner of a Rock-Paper-Scissors round.
    Returns:
        "player" if player wins,
        "opponent" if opponent wins,
        "draw" if it's a tie.
    """
    if player_move == opponent_move:
        return "draw"
    elif (player_move == "R" and opponent_move == "S") or \
         (player_move == "R" and opponent_move == "P") or \
         (player_move == "P" and opponent_move == "R"):
        return "player"
    else:
        return "opponent"