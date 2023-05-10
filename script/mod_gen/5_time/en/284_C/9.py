def main():
    n,m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(n - m)

if __name__ == '__main__':
    main()