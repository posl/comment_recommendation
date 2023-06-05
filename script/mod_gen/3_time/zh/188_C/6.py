def get_second_place(players):
    players.sort()
    second_place = players[1]
    return second_place

if __name__ == '__main__':
    get_second_place()