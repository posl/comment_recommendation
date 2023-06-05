def solve(n, s):
    if n == 1:
        return 2
    if s[n - 2] == "OR":
        return 2 ** n - 1
    else:
        return 2 ** n - 2
n = int(input())
s = []
for _ in range(n):
    s.append(input())
print(solve(n, s))
