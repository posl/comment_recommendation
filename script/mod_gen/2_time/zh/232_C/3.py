def problem232_b():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, 26):
        tmp = ""
        for j in range(len(s)):
            if ord(s[j]) + i > 122:
                tmp += chr(ord(s[j]) + i - 26)
            else:
                tmp += chr(ord(s[j]) + i)
        if tmp == t:
            print("Yes")
            return
    print("No")
    return
problem232_b()
