def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if balls[AB[j][0]-1] >= 1 and balls[AB[j][1]-1] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
