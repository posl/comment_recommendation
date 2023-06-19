def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        print("Yes")
        return
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            print("No")
            return
    print("Yes")
solve()
