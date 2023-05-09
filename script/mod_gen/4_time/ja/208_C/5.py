def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k >= n:
        for i in range(n):
            print(k // n)
    else:
        b = [0 for i in range(n)]
        for i in range(k):
            b[i] = 1
        for i in range(n):
            print(b[a[i] - 1])

if __name__ == '__main__':
    main()