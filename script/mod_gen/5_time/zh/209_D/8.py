def main():
    n, q = [int(i) for i in input().split()]
    roads = []
    for i in range(n-1):
        a, b = [int(i) for i in input().split()]
        roads.append((a, b))
    queries = []
    for i in range(q):
        c, d = [int(i) for i in input().split()]
        queries.append((c, d))
    for query in queries:
        c, d = query
        if (c, d) in roads or (d, c) in roads:
            print("Road")
        else:
            print("Town")

if __name__ == '__main__':
    main()