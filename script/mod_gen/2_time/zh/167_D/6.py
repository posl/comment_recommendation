def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    b[0] = 1
    c = 0
    for i in range(1, n+1):
        c = a[c] - 1
        if b[c] > 0:
            break
        else:
            b[c] = i + 1
    if i == n:
        print(c+1)
    else:
        d = i - b[c] + 1
        e = (k - i) % d
        for i in range(e):
            c = a[c] - 1
        print(c+1)

if __name__ == '__main__':
    main()