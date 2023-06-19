def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(range(n))
    b.sort(key=lambda i: a[i])
    c = [0] * n
    for i in range(n):
        c[b[i]] = k // n
        if i < k % n:
            c[b[i]] += 1
    for i in range(n):
        print(c[i])

if __name__ == '__main__':
    main()