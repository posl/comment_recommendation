def get_input():
    N, Q = map(int, input().split())
    t = []
    a = []
    b = []
    for i in range(Q):
        t1, a1, b1 = map(int, input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    return N, Q, t, a, b

if __name__ == '__main__':
    get_input()