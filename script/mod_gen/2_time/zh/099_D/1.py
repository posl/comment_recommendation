def min_cost():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    cc = [list(map(int, input().split())) for _ in range(n)]
    mod = [[0 for _ in range(c)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            mod[(i+j)%3][cc[i][j]-1] += 1
    ans = 10**9
    for i in range(c):
        for j in range(c):
            if i==j:
                continue
            for k in range(c):
                if i==k or j==k:
                    continue
                cost = 0
                for l in range(c):
                    cost += d[l][i]*mod[0][l]
                    cost += d[l][j]*mod[1][l]
                    cost += d[l][k]*mod[2][l]
                ans = min(ans, cost)
    print(ans)
min_cost()
