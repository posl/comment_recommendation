def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    #print(B)
    ans = 0
    for i in range(N):
        ans += B[i] * (B[i]-1) // 2
    #print(ans)
    for i in range(N):
        print(ans - B[A[i]-1] + 1)
