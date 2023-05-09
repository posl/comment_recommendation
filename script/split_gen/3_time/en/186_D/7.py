def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = [0]*(N+1)
    for i in range(1,N+1):
        B[i] = B[i-1]+A[i-1]
    ans = 0
    for i in range(N):
        ans += (i+1)*A[i]-B[i]
    print(2*ans)
