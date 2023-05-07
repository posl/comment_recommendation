def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            tmp = 0
            for k in range(i):
                tmp += V[k]
            for k in range(j):
                tmp += V[N-1-k]
            tmp += max(0,K-i-j)
            ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()