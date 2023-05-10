def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        tmp = [0]*(N+1)
        for j in range(K):
            if (i>>j)&1:
                tmp[CD[j][0]] += 1
            else:
                tmp[CD[j][1]] += 1
        cnt = 0
        for m in range(M):
            if tmp[AB[m][0]] >= 1 and tmp[AB[m][1]] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
