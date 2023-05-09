def get_input():
    n, q = map(int, input().split())
    l = list()
    a = list()
    for _ in range(n):
        l.append(int(input().split()[0]))
        a.append(list(map(int, input().split())))
    s = list()
    t = list()
    for _ in range(q):
        s_i, t_i = map(int, input().split())
        s.append(s_i)
        t.append(t_i)
    return n, q, l, a, s, t

if __name__ == '__main__':
    get_input()