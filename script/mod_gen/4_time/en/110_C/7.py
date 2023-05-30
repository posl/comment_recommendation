def solve(s, t):
    return 'Yes' if set(s) == set(t) else 'No'
s = input()
t = input()
print(solve(s, t))
