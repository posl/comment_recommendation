def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            c = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    c += 1
            if c == m:
                ans += 1
    print(ans)
