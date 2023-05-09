def solve():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    c = [0] * n
    d = [0] * n
    for i in range(n):
        if s[i] == '(':
            a[i] = 1
        elif s[i] == ')':
            b[i] = 1
        elif s[i].islower():
            c[i] = 1
    for i in range(n - 1, -1, -1):
        if b[i] == 0:
            d[i] = 1
        if i < n - 1:
            d[i] += d[i + 1]
    for i in range(n):
        if c[i] == 1 and d[i] == 0:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()