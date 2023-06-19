def solve(n, x, s):
    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans = ans * 2
        elif s[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = (ans - 1) // 2
    return ans
n, x = map(int, input().split())
s = input()
print(solve(n, x, s))
