def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print("Yes")
            return
    print("No")
solve()
