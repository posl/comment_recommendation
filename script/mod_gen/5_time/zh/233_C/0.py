def get_input():
    n, x = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
        a.append(l[i][1:])
    return n, x, l, a

if __name__ == '__main__':
    get_input()