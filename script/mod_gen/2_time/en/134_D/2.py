def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(b[i::i + 1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1)

if __name__ == '__main__':
    main()