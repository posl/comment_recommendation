def main():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    CD = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        balls = [0] * (n + 1)
        for j in range(k):
            if i >> j & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        cnt = 0
        for a, b in AB:
            if balls[a] and balls[b]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
