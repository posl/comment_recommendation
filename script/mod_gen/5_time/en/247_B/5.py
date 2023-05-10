def get_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    return n, s, t

if __name__ == '__main__':
    get_input()