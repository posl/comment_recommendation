def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    sumA = sum(A)
    for i in range(N):
        sumA -= A[i]
        ans += A[i] * sumA
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()