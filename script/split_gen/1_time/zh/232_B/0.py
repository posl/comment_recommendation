def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
solve()
