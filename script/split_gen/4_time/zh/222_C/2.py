def get_winner(player1, player2):
    if player1 == player2:
        return player1
    elif player1 == 'G':
        if player2 == 'C':
            return player1
        else:
            return player2
    elif player1 == 'C':
        if player2 == 'P':
            return player1
        else:
            return player2
    elif player1 == 'P':
        if player2 == 'G':
            return player1
        else:
            return player2
