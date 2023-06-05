def get_input():
    n, q = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
        a.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(q):
        s_t = list(map(int, input().split()))
        s.append(s_t[0])
        t.append(s_t[1])
    return n, q, l, a, s, t

if __name__ == '__main__':
    get_input()