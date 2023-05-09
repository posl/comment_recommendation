def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")
    return
