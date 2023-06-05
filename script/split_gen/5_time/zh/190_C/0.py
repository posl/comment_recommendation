def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for a, b in AB:
            if dish[a-1] > 0 and dish[b-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
