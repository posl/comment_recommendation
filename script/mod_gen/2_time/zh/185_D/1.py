def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    if N == 1:
        print(1)
        return
    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)
    k = 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] - 1 > k:
            k = A[i] - A[i-1] - 1
    ans = 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] - 1 == k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()