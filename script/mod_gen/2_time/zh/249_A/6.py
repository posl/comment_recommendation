def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        l = query[0] - 1
        r = query[1]
        x = query[2]
        print(a[l:r].count(x))

if __name__ == '__main__':
    main()