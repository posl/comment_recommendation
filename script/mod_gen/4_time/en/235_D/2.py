def main():
    a, N = map(int, input().split())
    if N < 10:
        if N == a:
            print(1)
        else:
            print(-1)
    else:
        count = 1
        x = a
        while x < N:
            x *= a
            count += 1
        if x == N:
            print(count)
        else:
            print(-1)

if __name__ == '__main__':
    main()