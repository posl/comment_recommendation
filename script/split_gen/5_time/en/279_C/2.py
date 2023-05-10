def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = [0]*H
    t = [0]*H
    for i in range(H):
        s[i] = ''.join(sorted(S[i]))
        t[i] = ''.join(sorted(T[i]))
    s.sort()
    t.sort()
    for i in range(H):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')
    return
