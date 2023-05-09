def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(M):
        ans = min(ans, A[-1-i]//2**i)
    print(ans)
