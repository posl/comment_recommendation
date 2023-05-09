def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(Q):
        s_i, t_i = map(int, input().split())
        s.append(s_i)
        t.append(t_i)
    for i in range(Q):
        print(L[s[i] - 1][t[i]])
