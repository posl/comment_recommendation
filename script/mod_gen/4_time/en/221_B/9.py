def solve(s,t):
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        if s[i] != t[i]:
            s[i], s[i+1] = s[i+1], s[i]
            break
    return "Yes" if s == t else "No"
s = input()
t = input()
print(solve(s,t))

if __name__ == '__main__':
    solve()