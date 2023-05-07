def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    b = [a[i] - a[i - 1] for i in range(1, n)]
    b = sorted(b, reverse=True)
    print(sum(a[m - 1:]) - sum(b[:m - 1]))

if __name__ == '__main__':
    main()