def main():
    a, N = map(int, input().split())
    if N == 1:
        print(0)
        return
    if a == 1:
        print(N - 1)
        return
    c = 1
    x = a
    while x < N:
        x *= a
        c += 1
    if x == N:
        print(c)
        return
    x //= a
    c -= 1
    if x == 1:
        print(-1)
        return
    while x % a == 0:
        x //= a
        c -= 1
    if x == 1:
        print(c)
        return
    if x % 10 == 1:
        x //= 10
        c -= 1
    if x == 1:
        print(c)
        return
    if x % 10 == 1:
        x //= 10
        c -= 1
    if x == 1:
        print(c)
        return
    print(-1)

if __name__ == '__main__':
    main()