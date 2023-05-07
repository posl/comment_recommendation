def main():
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    p.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (p[j][1] - p[i][1]) / (p[j][0] - p[i][0]) <= 1:
                ans += 1
    print(ans)
