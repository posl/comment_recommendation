def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        l, r, x = map(int, input().split())
        queries.append((l, r, x))
    for query in queries:
        l, r, x = query
        print(a[l-1:r].count(x))

if __name__ == '__main__':
    main()