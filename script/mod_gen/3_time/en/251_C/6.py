def solve():
    n = int(input())
    s = [input().split() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i][0] in d:
            d[s[i][0]] = max(d[s[i][0]], int(s[i][1]))
        else:
            d[s[i][0]] = int(s[i][1])
    ans = 0
    for i in range(n):
        if s[i][0] in d and d[s[i][0]] == int(s[i][1]):
            ans = i + 1
            break
    print(ans)

if __name__ == '__main__':
    solve()