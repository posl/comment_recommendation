def solve():
    s = input()
    t = input()
    n = len(s)
    if n != len(t):
        return "No"
    for i in range(n):
        if s[i] != t[i]:
            return "No"
    return "Yes"
print(solve())
