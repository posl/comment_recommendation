def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j] or s[i][4:] == t[j] or s[i][5:] == t[j]:
                ans += 1
    print(ans)
