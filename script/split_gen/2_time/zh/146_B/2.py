def problem146_b():
    n = int(input())
    s = input()
    s1 = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s1 += chr(ord(s[i]) + n - 26)
        else:
            s1 += chr(ord(s[i]) + n)
    print(s1)
problem146_b()
