def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    for i in range(N-1):
        ans += abs(A[i]-A[i+1])
    for i in range(N):
        if i == 0:
            ans -= abs(A[i])
            ans -= abs(A[i+1])
            ans += abs(A[i+1]-A[i])
        elif i == N-1:
            ans -= abs(A[i])
            ans -= abs(A[i-1])
            ans += abs(A[i]-A[i-1])
        else:
            ans -= abs(A[i])
            ans -= abs(A[i-1])
            ans -= abs(A[i+1])
            ans += abs(A[i+1]-A[i-1])
        print(ans)
