def main():
    n = int(input())
    a = [int(_) for _ in input().split()]
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append([int(_) for _ in input().split()])
    for query in queries:
        l, r, x = query
        print(a[l-1:r].count(x))

if __name__ == '__main__':
    main()