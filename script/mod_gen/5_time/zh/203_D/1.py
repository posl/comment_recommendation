def main():
    n,k = map(int,input().split())
    A = []
    for _ in range(n):
        A.append(list(map(int,input().split())))
    #print(A)
    ans = 1000000000
    for i in range(n-k+1):
        for j in range(n-k+1):
            tmp = []
            for l in range(k):
                for m in range(k):
                    tmp.append(A[i+l][j+m])
            tmp.sort()
            ans = min(ans,tmp[(k*k)//2])
    print(ans)

if __name__ == '__main__':
    main()