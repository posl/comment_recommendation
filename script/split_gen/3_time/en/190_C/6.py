def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for bit in range(1 << K):
        dish = [0] * (N + 1)
        for i in range(K):
            if bit & (1 << i):
                dish[CD[i][1]] += 1
            else:
                dish[CD[i][0]] += 1
        cnt = 0
        for a, b in AB:
            if dish[a] >= 1 and dish[b] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
