def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(AB)
    K = int(input())
    #print(K)
    CD = [list(map(int, input().split())) for _ in range(K)]
    #print(CD)
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        #print(balls)
        cnt = 0
        for k in range(M):
            if balls[AB[k][0]] > 0 and balls[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
