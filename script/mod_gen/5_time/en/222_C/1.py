def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2*n)]
    players = [i for i in range(2*n)]
    for i in range(m):
        players = sorted(players, key=lambda x: (a[x][i], x))
        for j in range(0, 2*n, 2):
            if a[players[j]][i] == 'G' and a[players[j+1]][i] == 'C':
                players[j+1], players[j] = players[j], players[j+1]
            elif a[players[j]][i] == 'C' and a[players[j+1]][i] == 'P':
                players[j+1], players[j] = players[j], players[j+1]
            elif a[players[j]][i] == 'P' and a[players[j+1]][i] == 'G':
                players[j+1], players[j] = players[j], players[j+1]
    for player in players:
        print(player+1)

if __name__ == '__main__':
    main()