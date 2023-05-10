def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[0:-1]
    print("No")
