def solve():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if rev:
                a = a + n if a <= n else a - n
                b = b + n if b <= n else b - n
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            rev = not rev
    if rev:
        s = s[n:] + s[:n]
    print(''.join(s))

if __name__ == '__main__':
    solve()