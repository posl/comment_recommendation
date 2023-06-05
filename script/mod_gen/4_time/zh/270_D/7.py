def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(K-1,-1,-1):
        if N >= A[i]:
            ans += (N//A[i])*(i+1)
            N %= A[i]
    print(ans)

if __name__ == '__main__':
    main()