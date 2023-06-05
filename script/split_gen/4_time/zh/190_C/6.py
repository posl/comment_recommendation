def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    #print(N, M, AB, K, CD)
    ans = 0
    for i in range(2**K):
        #print("i=", i)
        balls = [0] * N
        for j in range(K):
            #print("j=", j)
            if ((i >> j) & 1):
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        #print(balls)
        tmp = 0
        for k in range(M):
            if balls[AB[k][0]-1] >= 1 and balls[AB[k][1]-1] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
