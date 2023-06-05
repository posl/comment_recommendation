def get_second_winner(players):
    players.sort()
    players.reverse()
    first_winner = players.pop(0)
    second_winner = players.pop(0)
    second_winner = players.pop(0) if players[0] > second_winner else second_winner
    return second_winner

if __name__ == '__main__':
    get_second_winner()