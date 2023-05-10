def main():
    # Read from Standard Input
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    # Perform operations
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        a[i], a[i+1] = a[i+1], a[i]
        if a[i] == x[i]:
            a[i], a[i+1] = a[i+1], a[i]
    print(*a)

if __name__ == '__main__':
    main()