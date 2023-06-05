def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(a)
    print(b)
    # 争端的桥梁
    c = []
    for i in range(M):
        if a[i] == 1:
            c.append(b[i])
    print(c)
    # 争端的岛屿
    d = []
    for i in range(M):
        if b[i] in c:
            d.append(a[i])
        if a[i] in c:
            d.append(b[i])
    print(d)
    # 争端的岛屿和桥梁
    e = []
    for i in range(M):
        if a[i] in d and b[i] in d:
            e.append(i)
    print(e)
    # 争端的桥梁的索引
    print(len(e))

if __name__ == '__main__':
    main()