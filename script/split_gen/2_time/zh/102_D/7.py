def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i]+A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i]+A[i]
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = D[i]+A[i]
    E = [0]*(N+1)
    for i in range(N):
        E[i+1] = E[i]+A[i]
    for i in range(1,N+1):
        C[i] = max(C[i], C[i-1])
    for i in range(N-1,-1,-1):
        D[i] = min(D[i], D[i+1])
    ans = 10**18
    j = N
    for i in range(N+1):
        while j > 0 and B[i] + D[j] < B[N]//2:
            j -= 1
        if j > 0:
            ans = min(ans, max(B[i], B[N]-B[i]) - max(C[i], D[j]))
    print(ans)
