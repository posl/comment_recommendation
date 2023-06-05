def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = [query[1] for _ in range(n)]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        else:
            print(a[query[1] - 1])

if __name__ == '__main__':
    main()