def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    sum_A2 = sum([a ** 2 for a in A])
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] ** 2 - 2 * A[i] * (sum_A - A[i]) + sum_A2
        sum_A -= A[i]
        sum_A2 -= A[i] ** 2
    print(ans)

if __name__ == '__main__':
    main()