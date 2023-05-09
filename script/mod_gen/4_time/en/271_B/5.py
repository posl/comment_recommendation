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
        s.append(int(input()))
        t.append(int(input()))
    return n, q, l, a, s, t

if __name__ == '__main__':
    get_input()