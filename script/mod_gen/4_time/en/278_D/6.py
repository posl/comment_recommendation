def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] == 1:
            a = [query[1] for i in range(n)]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        elif query[0] == 3:
            print(a[query[1] - 1])

if __name__ == '__main__':
    main()