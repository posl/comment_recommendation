def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * (N+1)
    for i in range(N, 0, -1):
        if a[i-1] != sum(b[i::i]) % 2:
            b[i] = 1
    print(sum(b))
    if sum(b) > 0:
        print(*[i for i, x in enumerate(b) if x == 1])

if __name__ == '__main__':
    main()