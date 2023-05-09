def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    sum = 0
    for i in range(N-1):
        sum += A[i] * sum(A[i+1:N])
    print(sum%mod)

if __name__ == '__main__':
    main()