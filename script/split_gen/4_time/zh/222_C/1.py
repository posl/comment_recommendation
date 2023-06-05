def win(a, b):
    if a == 'G' and b == 'C':
        return True
    elif a == 'C' and b == 'P':
        return True
    elif a == 'P' and b == 'G':
        return True
    else:
        return False
n, m = map(int, input().split())
a = [input() for _ in range(2 * n)]
rank = [[i + 1, 0] for i in range(2 * n)]
for i in range(m):
    for j in range(n):
        p1, p2 = rank[2 * j][0] - 1, rank[2 * j + 1][0] - 1
        if win(a[p1][i], a[p2][i]):
            rank[2 * j][1] -= 1
        elif win(a[p2][i], a[p1][i]):
            rank[2 * j + 1][1] -= 1
    rank.sort(key=lambda x: (x[1], x[0]))
for i in range(2 * n):
    print(rank[i][0])
