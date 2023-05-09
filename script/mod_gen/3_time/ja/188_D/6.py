def get_input():
    n, c = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    return n, c, a, b, c

if __name__ == '__main__':
    get_input()