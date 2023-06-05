def solution():
    s = input()
    l = len(s)
    s = list(s)
    s.sort()
    if s[0] == s[-1]:
        print(s[0] * l)
        return
    if l == 2:
        print(s[0] + s[1])
        return
    if s[0] == s[1]:
        print(s[0] + s[2] * (l - 1))
        return
    else:
        print(s[0] + s[1] + s[2] * (l - 2))
        return
solution()
