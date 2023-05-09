def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k <= n:
        for i in range(n):
            if i < k:
                print(1)
            else:
                print(0)
        return
    k -= n
    m = k // (n - 1)
    k -= m * (n - 1)
    for i in range(n):
        if i == 0:
            print(m + 1)
        else:
            if i <= k:
                print(m + 2)
            else:
                print(m + 1)

if __name__ == '__main__':
    main()