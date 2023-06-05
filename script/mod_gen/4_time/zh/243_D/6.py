def solve(n, x, s):
    p = 1 << n
    for i in range(n):
        if s[i] == 'U':
            p = (p - 1) // 2
        elif s[i] == 'L':
            p = p * 2
        else:
            p = p * 2 + 1
    return p
n, x = map(int, input().split())
s = input()
print(solve(n, x, s))
