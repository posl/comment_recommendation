def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    t = n * m - total
    if t > k:
        print(-1)
    else:
        print(max(0, t))

if __name__ == '__main__':
    main()