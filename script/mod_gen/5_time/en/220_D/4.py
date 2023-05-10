def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*10
    ans[A[0]] = 1
    for i in range(1,N):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+A[i])%10] += ans[j]
            tmp[(j*A[i])%10] += ans[j]
        ans = tmp
    for i in ans:
        print(i%998244353)

if __name__ == '__main__':
    main()