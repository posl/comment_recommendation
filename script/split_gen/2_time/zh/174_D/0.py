def solve():
    n = int(input())
    c = input()
    ans = 0
    w = 0
    for i in range(n):
        if c[i] == 'W':
            w += 1
    for i in range(n):
        if i < w and c[i] == 'R':
            ans += 1
    print(ans)
solve()
