def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    for query in queries:
        x = query[0]
        k = query[1]
        count = 0
        for i in range(n):
            if a[i] == x:
                count += 1
            if count == k:
                print(i+1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()