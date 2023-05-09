def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        if M == 0:
            ans += A[i]
            continue
        if A[i] <= 2**M:
            ans += A[i]
        else:
            ans += A[i]//(2**M)
            M = 0
    print(ans)
