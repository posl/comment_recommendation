def solve():
    N, D = map(int, input().split())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i + 1
        while j < N and LR[i][1] >= LR[j][0]:
            j += 1
        i = j
        if i < N:
            i -= 1
            while i < N and LR[i][1] >= LR[i][0] + D:
                i += 1
    print(ans)
solve()
