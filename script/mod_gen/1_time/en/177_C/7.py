def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i * (N - 1 - i) + (N - 1 - i) * (N - 1 - i - 1) // 2)
        ans %= 10 ** 9 + 7
    print(ans)

if __name__ == '__main__':
    main()