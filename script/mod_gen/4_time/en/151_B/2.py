def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) <= k:
        print(max(n * m - sum(a), 0))
    else:
        print(-1)
main()

if __name__ == '__main__':
    main()