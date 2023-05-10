def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    if A[0] != 1:
        A.insert(0, 0)
    if A[M - 1] != N:
        A.append(N + 1)
    if M == 1:
        print(A[1] - A[0] - 1)
        return
    if M == 2:
        print(min(A[1] - A[0] - 1, A[2] - A[1] - 1))
        return
    ans = 0
    for i in range(1, M + 1):
        ans = max(ans, A[i] - A[i - 1] - 1)
    print(ans)
