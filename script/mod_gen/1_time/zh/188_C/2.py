def find_second_player(players):
    players.sort(reverse=True)
    players.pop(0)
    players.pop(0)
    return players[0]

if __name__ == '__main__':
    find_second_player()