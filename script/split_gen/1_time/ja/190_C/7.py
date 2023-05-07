def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        ball = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                ball[CD[j][1]] += 1
            else:
                ball[CD[j][0]] += 1
        cnt = 0
        for k in range(M):
            if ball[AB[k][0]] > 0 and ball[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
