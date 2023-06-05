def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = map(int, input().split())
    q = int(input())
    d = [0] * q
    l = [0] * q
    for i in range(q):
        d[i], l[i] = map(str, input().split())
    print(r, c, d, l)
    # r = [5, 2, 1]
    # c = [3, 2, 4]
    # d = ['L', 'U', 'L', 'R']
    # l = [2, 3, 2, 4]
    # h, w, r_s, c_s = 5, 5, 4, 4
    # n = 3
    # q = 4
    # r = [3, 4, 2, 3, 5, 1, 3]
    # c = [1, 3, 6, 4, 5, 1, 2]
    # d = ['D', 'U', 'L', 'D', 'U', 'D', 'U', 'R', 'L', 'D']
    # l = [3, 3, 2, 2, 3, 3, 3, 3, 3, 1]
    # h, w, r_s, c_s = 6, 6, 6, 3
    # n = 7
    # q = 10
    # r = [2, 5, 5, 4, 1, 2, 6, 4, 3, 4, 5, 3, 1, 2, 3, 4, 2, 5, 3, 1, 4, 2, 5, 1, 3, 6, 5, 3, 6, 4, 1, 2, 3, 4, 5, 6, 1, 3, 2, 4, 5

if __name__ == '__main__':
    main()