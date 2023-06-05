def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 10**9+7
    ans = 0
    for i in range(N):
        ans += A[i]*(sum(A[i+1:])%MOD)
    print(ans%MOD)

if __name__ == '__main__':
    main()