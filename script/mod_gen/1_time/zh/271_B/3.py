def get_input():
    n, q = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s_t = []
    for i in range(q):
        s_t.append(list(map(int, input().split())))
    return n, q, l, s_t

if __name__ == '__main__':
    get_input()