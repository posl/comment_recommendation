def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(M)
    B = [A[0]]
    for i in range(1,N+1):
        if A[i] != A[i-1]:
            B.append(A[i])
    N = len(B)
    D = [0] * N
    for i in range(N-1):
        D[i] = B[i+1] - B[i] - 1
    D[N-1] = M - B[N-1] + B[0] - 1
    D.sort()
    ans = 0
    for i in range(N-1):
        ans += D[i]
    print(ans)

if __name__ == '__main__':
    main()