def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i] * (N - i - 1)
    print(total % (10 ** 9 + 7))

if __name__ == '__main__':
    main()