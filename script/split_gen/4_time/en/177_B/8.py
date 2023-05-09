def solve():
    s = input()
    t = input()
    res = len(t)
    for i in range(len(s) - len(t) + 1):
        c = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                c += 1
        res = min(res, c)
    print(res)
