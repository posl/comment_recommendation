def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        for j in range(M):
            ans = min(ans,abs(A[i] - B[j]))
    print(ans)

if __name__ == '__main__':
    main()