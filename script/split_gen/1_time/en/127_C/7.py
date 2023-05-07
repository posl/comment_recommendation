def solve():
    # Implement solution here
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    l = max(L)
    r = min(R)
    if r < l:
        print(0)
    else:
        print(r - l + 1)
