import numpy as np

def simulate_takoyaki_game_probability(num_trials=10000):
    player1_wins = 0
    player2_wins = 0

    for _ in range(num_trials):
        # Create a deck with numbers 1 to 10, each number repeated five times
        deck = np.repeat(np.arange(1, 11), 5)
        np.random.shuffle(deck)

        player1_cards = set()
        player2_cards = set()
        player_turn = 1  # Player 1 starts

        while deck.size > 0:
            if deck.size == 0:
                break
            card = deck[0]
            deck = np.delete(deck, 0)

            if player_turn == 1:
                if card not in player1_cards:
                    player1_cards.add(card)
                    if len(player1_cards) == 10:
                        player1_wins += 1
                        break
                else:
                    player_turn = 2  # Switch turn if the card is already collected
            else:
                if card not in player2_cards:
                    player2_cards.add(card)
                    if len(player2_cards) == 10:
                        player2_wins += 1
                        break
                else:
                    player_turn = 1  # Switch turn if the card is already collected

    return player1_wins / num_trials, player2_wins / num_trials

# Run the simulation and get the probabilities of each player winning
print(simulate_takoyaki_game_probability())
