def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    s = s.replace('?', 'a')
    t = t.replace('?', 'a')
    for i in range(n - m + 1):
        if s[i:i + m] == t:
            print('Yes')
        else:
            print('No')
