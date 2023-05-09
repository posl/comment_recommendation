def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        l, r, x = map(int, input().split())
        queries.append([l, r, x])
    for query in queries:
        l = query[0]
        r = query[1]
        x = query[2]
        print(a[l-1:r].count(x))

if __name__ == '__main__':
    main()