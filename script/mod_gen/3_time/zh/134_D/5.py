def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    i = N
    while i > 0:
        if a[i - 1] == 1:
            b[i - 1] = 1
            j = 2
            while i * j <= N:
                a[i * j - 1] = 1 - a[i * j - 1]
                j += 1
        i -= 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1, end=' ')
    print()

if __name__ == '__main__':
    main()