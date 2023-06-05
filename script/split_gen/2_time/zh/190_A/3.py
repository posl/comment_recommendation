def solve(n, s):
    ans = 1
    for i in range(n):
        if s[i] == 'OR':
            ans += 2 ** (i+1)
    return ans
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(solve(n, s))
