def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = [0]*N
        for j in range(K):
            if i>>j&1:
                cnt[CD[j][0]-1] += 1
            else:
                cnt[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if cnt[AB[j][0]-1] > 0 and cnt[AB[j][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
