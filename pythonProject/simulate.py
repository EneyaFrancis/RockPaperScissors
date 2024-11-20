#Handles simulation of matches between players

from game_rules import decide_winner

def play_game(player1, player2, num_rounds=100, verbose=False):
   """
   Simulates a game between two players.
   Returns stats for the game.
   """
   stats = {
       "player1_score" : 0,
       "player2_score": 0,
       "draws": 0,
       "player1_moves" : {"R": 0, "P":0, "S":0},
       "player2_moves" : {"R": 0, "P":0, "S":0}
   }

   player1_prev, player2_prev = "", ""

   for _ in range(num_rounds):
       move1 = player1(player2_prev)
       move2 = player2(player1_prev)

       stats["player1_moves"][move1] += 1
       stats["player2_moves"][move2] += 1

       winner = decide_winner(move1, move2)
       if winner == "player":
           stats["player1_score"] += 1
       elif winner == "opponent":
           stats["player2_score"] += 1
       else:
           stats["draws"] += 1

       if verbose:
           print(f"Player 1: {move1} | Player 2: {move2} | Winner: {winner}")

       player1_prev, player2_prev = move1, move2
   return  stats