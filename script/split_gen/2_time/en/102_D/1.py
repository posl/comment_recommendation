def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i] + A[N-1-i]
    ans = 10**9
    for i in range(1,N-1):
        for j in range(2,N-i+1):
            ans = min(ans, max(B[i],B[i+j],C[N-i],C[N-i-j]) - min(B[i],B[i+j],C[N-i],C[N-i-j]))
    print(ans)
