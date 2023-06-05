def get_second_player(players):
    players.sort()
    players.reverse()
    return players[1]

if __name__ == '__main__':
    get_second_player()