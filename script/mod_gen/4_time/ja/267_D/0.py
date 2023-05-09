def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += (j+1)*A[i+j]
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()