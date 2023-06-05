def solve(n, x, s):
    cur = x
    for i in range(n):
        if s[i] == 'U':
            cur = (cur + 1) // 2
        elif s[i] == 'L':
            cur *= 2
        else:
            cur = cur * 2 + 1
    return cur
n, x = map(int, input().split())
s = input()
print(solve(n, x, s))
