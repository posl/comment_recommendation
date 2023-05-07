def get_input():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    return n, m, x, c, a

if __name__ == '__main__':
    get_input()