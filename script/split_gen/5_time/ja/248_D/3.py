def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X = Query[i][2]
        print(A[L-1:R].count(X))
