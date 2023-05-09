def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    table = []
    for i in range(N):
        p = P[i]
        if len(table) == 0:
            table.append([p, i])
        else:
            if table[-1][0] < p:
                table.append([p, i])
            else:
                while len(table) > 0 and table[-1][0] >= p:
                    ans[table[-1][1]] = i
                    table.pop()
                table.append([p, i])
    while len(table) > 0:
        ans[table[-1][1]] = -1
        table.pop()
    for i in range(N):
        print(ans[i])
