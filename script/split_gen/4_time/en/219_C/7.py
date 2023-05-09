def solve():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(x, 'abcdefghijklmnopqrstuvwxyz'))
    s.sort()
    for i in range(n):
        s[i] = s[i].translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', x))
        print(s[i])
