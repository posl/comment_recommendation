def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    B = [0] * N
    for i in range(N):
        B[i] = A[i+1] - A[i]
    B.sort()
    B = [0] + B
    #print(A)
    #print(B)
    C = [0] * (N+1)
    for i in range(N+1):
        C[i] = B[i] * i
    #print(C)
    for i in range(N):
        C[i+1] += C[i]
    #print(C)
    ans = 0
    for i in range(N+1):
        if K >= B[i]:
            ans = max(ans, C[i] + (K-B[i])*(N-i))
    print(ans)
