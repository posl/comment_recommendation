def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = []
    t = []
    for i in range(H):
        s1 = []
        t1 = []
        for j in range(W):
            if S[i][j] == '#':
                s1.append(j)
            if T[i][j] == '#':
                t1.append(j)
        s.append(s1)
        t.append(t1)
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')
