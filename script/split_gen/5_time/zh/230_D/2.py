def solve():
    N, D = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(N)]
    LRs.sort(key=lambda x: x[0])
    LRs = [[0, 0]] + LRs
    LRs.append([10 ** 9 + 1, 10 ** 9 + 1])
    ans = 0
    for i in range(1, N + 2):
        if LRs[i][0] - LRs[i - 1][1] >= D:
            ans += 1
        elif LRs[i][0] - LRs[i - 1][1] < D and LRs[i][0] - LRs[i - 1][1] > 0:
            ans += 2
        else:
            pass
    print(ans)
