def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1, -1, -1):
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i+1 for i in range(n) if b[i] == 1])

if __name__ == '__main__':
    main()