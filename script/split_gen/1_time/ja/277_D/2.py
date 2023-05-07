def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(sum(A))
        return
    if A[-1] == M-1:
        print(0)
        return
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    B = B[1:]
    ans = 10**10
    for i in range(N):
        if A[i] != A[i+1]:
            ans = min(ans, (A[i]+1) * i - B[i] + B[-1] - B[i+1] - (M-1-A[i]) * (N-i-1))
    print(ans)
