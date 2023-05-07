def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k <= n:
        print(k)
        for i in range(n - k):
            print(0)
        return
    b = [0] * n
    for i in range(n):
        b[i] = k // n
    for i in range(k % n):
        b[i] += 1
    for i in range(n):
        b[i] += (n - a[i]) // n
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    main()