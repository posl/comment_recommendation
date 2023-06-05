def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] == A[j]:
                ans += 1
                ans %= mod
            elif (A[i]+A[j])%2 == 0:
                mid = (A[i]+A[j])//2
                if mid in A:
                    ans += 1
                    ans %= mod
    print(ans)
main()
