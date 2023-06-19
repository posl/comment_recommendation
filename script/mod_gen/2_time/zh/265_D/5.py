def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    max_p = A[0]
    min_p = A[0]
    max_q = A[0]
    min_q = A[0]
    max_r = A[0]
    min_r = A[0]
    for i in range(1, N):
        max_p = max(max_p, A[i])
        min_p = min(min_p, A[i])
        max_q = max(max_q, A[i] + max_p - P)
        min_q = min(min_q, A[i] + min_p - P)
        max_r = max(max_r, A[i] + max_q - Q)
        min_r = min(min_r, A[i] + min_q - Q)
    if max_r == R and min_r == R:
        print("Yes")
    else:
        print("No")
solve()
