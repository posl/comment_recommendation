def solve():
    s = input()
    n = len(s)
    r = 0
    b = 0
    for i in range(n):
        if s[i] == '0':
            r += 1
        else:
            b += 1
    print(min(r,b)*2)
