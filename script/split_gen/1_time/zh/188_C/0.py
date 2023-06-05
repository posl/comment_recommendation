def get_second_player(n, a):
    players = [i for i in range(1, 2 ** n + 1)]
    while len(players) > 2:
        players = [max(players[i], players[i + 1]) for i in range(0, len(players), 2)]
    return min(players)
n = int(input())
a = list(map(int, input().split()))
print(get_second_player(n, a))
