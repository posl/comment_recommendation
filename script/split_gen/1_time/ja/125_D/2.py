def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    B[0] = A[0]
    for i in range(1,N):
        B[i] = B[i-1] + A[i]
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N-1):
        ans += A[i]
    ans += B[N-1]
    print(ans)
