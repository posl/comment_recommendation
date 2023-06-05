def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ab.append([m+1, 0])
    ans = 0
    now = 0
    for i in range(n):
        if ab[i][0] != ab[i+1][0]:
            ans += ab[i][1]
        else:
            now += ab[i][1]
        if ab[i][0] != ab[i+1][0] or i == n-1:
            if now < ans:
                now = ans
    print(now)

if __name__ == '__main__':
    solve()