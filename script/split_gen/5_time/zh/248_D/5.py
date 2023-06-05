def solve():
    #请在这里编写代码
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))
