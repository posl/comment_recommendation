def solve():
    N = int(input())
    A = []
    x = []
    y = []
    for i in range(N):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            a, b = map(int, input().split())
            x[i].append(a)
            y[i].append(b)
    ans = 0
    for bit in range(1 << N):
        flag = True
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                cnt += 1
                for j in range(A[i]):
                    if y[i][j] == 1 and not bit & (1 << (x[i][j] - 1)):
                        flag = False
        if flag:
            ans = max(ans, cnt)
    print(ans)
solve()
