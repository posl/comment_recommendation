def fun():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if ord(s[i]) - ord(t[i]) >= 0:
            if ord(s[i]) - ord(t[i]) > 1:
                print("No")
                return
        else:
            if ord(s[i]) - ord(t[i]) < -1:
                print("No")
                return
    print("Yes")
    return
