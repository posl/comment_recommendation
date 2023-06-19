def find_second_player(players):
    if len(players) == 2:
        return players[0] if players[0] < players[1] else players[1]
    else:
        winners = []
        for i in range(0, len(players), 2):
            if players[i] < players[i + 1]:
                winners.append(players[i + 1])
            else:
                winners.append(players[i])
        return find_second_player(winners)

if __name__ == '__main__':
    find_second_player()