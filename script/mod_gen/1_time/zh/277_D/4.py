def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(M)
    B = []
    for i in range(N):
        if A[i] != A[i+1]:
            B.append(A[i])
    B.append(M)
    L = len(B)
    ans = 0
    for i in range(L-1):
        if (B[i+1]-B[i])%M != 1:
            ans += B[i]
    print(ans)

if __name__ == '__main__':
    main()