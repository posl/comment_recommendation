def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + '(' + str(d[s[i]]-1) + ')')
        else:
            d[s[i]] = 1
            print(s[i])
