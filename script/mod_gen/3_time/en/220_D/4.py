def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0]*10
    for i in range(10):
        ans[i] = pow(2, N-1, MOD)
    for i in range(N):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+A[i])%10] += ans[j]
            tmp[(j*A[i])%10] += ans[j]
        for j in range(10):
            ans[j] = tmp[j]%MOD
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()