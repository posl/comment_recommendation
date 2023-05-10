def solve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i - k] == 'r':
                t[i] = 'x'
            else:
                ans += p
        elif t[i] == 's':
            if i >= k and t[i - k] == 's':
                t[i] = 'x'
            else:
                ans += r
        else:
            if i >= k and t[i - k] == 'p':
                t[i] = 'x'
            else:
                ans += s
    print(ans)

if __name__ == '__main__':
    solve()