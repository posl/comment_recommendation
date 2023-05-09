def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(1 << K):
        cnt = [0] * (N + 1)
        for j in range(K):
            if i >> j & 1:
                cnt[CD[j][1]] += 1
            else:
                cnt[CD[j][0]] += 1
        tmp = 0
        for j in range(M):
            if cnt[AB[j][0]] > 0 and cnt[AB[j][1]] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    solve()