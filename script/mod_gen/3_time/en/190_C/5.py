def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        d = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                d[CD[j][1]] += 1
            else:
                d[CD[j][0]] += 1
        cnt = 0
        for a, b in AB:
            if d[a] > 0 and d[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    solve()