def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        s = sum(b[i::i]) % 2
        if s != a[i - 1]:
            b[i] = 1
    print(sum(b))
    print(*[i for i, v in enumerate(b) if v][1:])

if __name__ == '__main__':
    main()