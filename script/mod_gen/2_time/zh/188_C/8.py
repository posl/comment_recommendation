def get_second_player(n, players):
    players.sort()
    #print(players)
    #print(players[n-1])
    #print(players[n])
    return players[n-1]

if __name__ == '__main__':
    get_second_player()