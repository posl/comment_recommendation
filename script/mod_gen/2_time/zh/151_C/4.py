def get_input():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_, s_ = input().split()
        p.append(int(p_))
        s.append(s_)
    return n, m, p, s

if __name__ == '__main__':
    get_input()