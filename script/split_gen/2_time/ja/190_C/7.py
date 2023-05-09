def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]
    K = int(input())
    CDs = [[*map(int, input().split())] for _ in range(K)]
    # compute
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CDs[j][1]] += 1
            else:
                balls[CDs[j][0]] += 1
        cnt = 0
        for AB in ABs:
            if balls[AB[0]] > 0 and balls[AB[1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    # output
    print(ans)
