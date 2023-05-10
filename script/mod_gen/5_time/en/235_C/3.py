def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        if a.count(x) < k:
            print(-1)
        else:
            print(a.index(x, k-1) + 1)

if __name__ == '__main__':
    main()