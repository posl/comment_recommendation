def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sumA = sum(A)
    for i in range(N):
        sumA -= A[i]
        ans += A[i]**2 * (N-1) - 2 * A[i] * sumA
    print(ans)

if __name__ == '__main__':
    main()