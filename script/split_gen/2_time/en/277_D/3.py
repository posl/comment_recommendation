def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = (B[i] + A[i]) % M
    ans = 0
    for i in range(N-1,-1,-1):
        if A[i] == A[i-1]:
            continue
        if A[i] == M-1:
            continue
        if A[i] == M-2:
            ans += A[i] + 1
            continue
        if A[i] == M-3:
            ans += A[i] + 2
            continue
        if B[i+1] == 0:
            continue
        if B[i] == 0:
            ans += A[i] + 1
            continue
        if B[i] == 1:
            ans += A[i] + 2
            continue
        if B[i] == 2:
            ans += A[i] + 3
            continue
        if B[i] > 2:
            ans += A[i] + 4
            continue
    print(ans)
