def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                ans += (A[i]+A[j]+A[k])%998244353
    print(ans%998244353)
