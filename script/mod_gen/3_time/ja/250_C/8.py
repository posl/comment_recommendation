def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in x:
        a[i-1], a[i] = a[i], a[i-1]
    print(*a)

if __name__ == '__main__':
    main()