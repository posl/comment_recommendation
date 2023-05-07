def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    ans = 0
    for i in range(1,N+1):
        if B[i] > 0:
            ans += B[i] * (B[i]-1) // 2
    print(ans)
