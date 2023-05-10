def rank_players(n, m, a):
    players = list(range(2*n))
    for i in range(m):
        new_players = []
        for j in range(n):
            p1 = players[2*j]
            p2 = players[2*j+1]
            if a[p1][i] == a[p2][i]:
                new_players.append(min(p1, p2))
            elif a[p1][i] == 'G' and a[p2][i] == 'C':
                new_players.append(p1)
            elif a[p1][i] == 'C' and a[p2][i] == 'P':
                new_players.append(p1)
            elif a[p1][i] == 'P' and a[p2][i] == 'G':
                new_players.append(p1)
            else:
                new_players.append(p2)
        players = new_players
    return players

if __name__ == '__main__':
    rank_players()