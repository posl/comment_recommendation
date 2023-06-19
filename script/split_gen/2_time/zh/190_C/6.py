def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        cnt = 0
        balls = set()
        for j in range(k):
            if (i >> j) & 1:
                balls.add(cd[j][0])
            else:
                balls.add(cd[j][1])
        for a, b in ab:
            if a in balls and b in balls:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
