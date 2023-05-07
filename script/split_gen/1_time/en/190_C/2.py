def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                cnt[CD[j][1]-1] += 1
            else:
                cnt[CD[j][0]-1] += 1
        ans = max(ans, sum([1 for a, b in AB if cnt[a-1] > 0 and cnt[b-1] > 0]))
    print(ans)
