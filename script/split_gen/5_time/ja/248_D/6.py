def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))
