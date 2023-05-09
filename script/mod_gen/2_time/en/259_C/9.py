def solve(s,t):
    if len(s) < len(t):
        return "No"
    for i in range(len(s)):
        if i == len(t):
            return "Yes"
        if s[i] != t[i]:
            if i == 0 or s[i-1] != t[i]:
                return "No"
    return "Yes"
s = input()
t = input()
print(solve(s,t))

if __name__ == '__main__':
    solve()