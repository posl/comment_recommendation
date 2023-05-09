def main():
    N = int(input())
    p = [tuple(map(int, input().split())) for _ in range(N)]
    p.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (p[i][1] - p[j][1]) / (p[i][0] - p[j][0]) <= 1:
                ans += 1
    print(ans)
