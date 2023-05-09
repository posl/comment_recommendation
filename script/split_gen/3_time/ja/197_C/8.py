def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**30
    for i in range(N):
        for j in range(i,N):
            ors = 0
            for k in range(i,j+1):
                ors |= A[k]
            ans = min(ans,ors)
    print(ans)
main()
