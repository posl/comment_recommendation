def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if K == 0:
        for i in range(N):
            if A[i] != B[i]:
                print("No")
                return
        print("Yes")
        return
    for i in range(N):
        if A[i] > B[i]:
            print("No")
            return
    print("Yes")
    return
solve()
