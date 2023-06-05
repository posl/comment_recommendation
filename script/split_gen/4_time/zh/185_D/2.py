def solve():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int, input().split()))
    A.sort()
    A.append(A[-1] + 1)
    if A[0] != 1:
        A.insert(0, 0)
    ans = 0
    for i in range(M + 1):
        if A[i + 1] - A[i] != 1:
            ans += 1
    print(ans)
solve()
