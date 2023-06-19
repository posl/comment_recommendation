def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        ball = [0] * n
        cnt = 0
        for j in range(k):
            if (i >> j) & 1:
                ball[cd[j][0]-1] += 1
            else:
                ball[cd[j][1]-1] += 1
        for a, b in ab:
            if ball[a-1] and ball[b-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
