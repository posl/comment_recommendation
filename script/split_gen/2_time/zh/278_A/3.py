def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        if A[i] < M-1:
            ans += A[i]
        else:
            ans += M-1
    print(ans)
