def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X -= A[i] * B[i]
    if X >= 0:
        print("Yes")
    else:
        print("No")
