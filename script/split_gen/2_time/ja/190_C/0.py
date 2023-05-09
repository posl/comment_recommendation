def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][1]] += 1
            else:
                balls[CD[j][0]] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]] >= 1 and balls[AB[j][1]] >= 1:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)
