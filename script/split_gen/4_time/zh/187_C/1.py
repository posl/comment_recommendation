def solve():
    n = int(input())
    s = [input() for i in range(n)]
    s = set(s)
    for x in s:
        if x[0] == '!':
            if x[1:] in s:
                print(x[1:])
