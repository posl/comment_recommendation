def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n)[::-1]:
        s = sum(b[i::i+1]) % 2
        if s != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i+1 for i, v in enumerate(b) if v])

if __name__ == '__main__':
    main()