def f(i):
    if i == 'G':
        return 0
    elif i == 'C':
        return 1
    elif i == 'P':
        return 2
    else:
        print("error")
n, m = map(int, input().split())
a = [0] * (2 * n)
for i in range(2 * n):
    a[i] = list(map(f, input()))
rank = [0] * (2 * n)
for i in range(2 * n):
    rank[i] = [0, i]
for i in range(m):
    for j in range(n):
        if a[rank[2 * j][1]][i] == a[rank[2 * j + 1][1]][i]:
            continue
        elif (a[rank[2 * j][1]][i] + 1) % 3 == a[rank[2 * j + 1][1]][i]:
            rank[2 * j][0] -= 1
        else:
            rank[2 * j + 1][0] -= 1
    rank.sort()
for i in range(2 * n):
    print(rank[i][1] + 1)
