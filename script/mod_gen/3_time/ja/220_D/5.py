def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = [0]*10
    for i in range(10):
        tmp = 0
        for j in range(N):
            if i == A[j]:
                tmp += pow(2,N-j-1,mod)
        ans[i] = tmp%mod
    print(*ans,sep='
')

if __name__ == '__main__':
    main()