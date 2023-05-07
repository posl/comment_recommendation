def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N,A)
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1,N):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j+A[i])%10] += ans[j]
            tmp[(j*A[i])%10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i]%998244353)

if __name__ == '__main__':
    main()