def main():
    l = int(input())
    n = 0
    m = 0
    edges = []
    for i in range(20):
        if l & (1 << i):
            edges.append((i+1, i+2, 0))
            edges.append((i+1, i+2, 1 << i))
            n = i+2
            m += 2
    for i in range(19):
        if l & (1 << i):
            edges.append((i+1, i+2, (1 << i) - 1))
            n = i+2
            m += 1
    print(n, m)
    for u, v, w in edges:
        print(u, v, w)

if __name__ == '__main__':
    main()