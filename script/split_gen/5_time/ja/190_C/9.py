def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = [0]*N
        for j in range(K):
            if (i>>j)&1:
                cnt[CD[j][0]-1] += 1
            else:
                cnt[CD[j][1]-1] += 1
        tmp = 0
        for a, b in AB:
            if cnt[a-1] and cnt[b-1]:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
