def solve():
    n = int(input())
    s = input()
    t = ""
    c = 0
    for i in range(n):
        if s[i] == '"':
            c += 1
            if c % 2 == 1:
                t += '"'
            else:
                t += '.'
        else:
            t += s[i]
    print(t)
