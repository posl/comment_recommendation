def main():
    n, q = map(int, input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    a = list(range(1, n+1))
    for i in range(q-1, -1, -1):
        a[i], a[i+1] = a[i+1], a[i]
        if a[i] == x[i]:
            a[i], a[i+1] = a[i+1], a[i]
    print(*a)

if __name__ == '__main__':
    main()