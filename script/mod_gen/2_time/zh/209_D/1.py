def main():
    n, q = map(int, input().split())
    roads = []
    for i in range(n-1):
        a, b = map(int, input().split())
        roads.append((a, b))
    for i in range(q):
        c, d = map(int, input().split())
        if (c, d) in roads or (d, c) in roads:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()