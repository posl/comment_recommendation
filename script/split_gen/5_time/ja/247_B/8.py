def get_input():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    return n, s, t
