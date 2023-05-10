def get_first_place(players):
    if len(players) == 1:
        return players[0]
    else:
        new_players = []
        for i in range(0, len(players), 2):
            new_players.append(max(players[i], players[i+1]))
        return get_first_place(new_players)

if __name__ == '__main__':
    get_first_place()