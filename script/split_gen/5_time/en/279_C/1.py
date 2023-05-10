def solve():
    h,w = map(int, input().split())
    s = []
    t = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        t.append(input())
    for i in range(h):
        if s[i] != t[i]:
            s[i] = ''.join(sorted(s[i]))
            t[i] = ''.join(sorted(t[i]))
    for i in range(h):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')
    return
