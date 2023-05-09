def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(i) for i in input().split()])
    for query in queries:
        L, R, X = query
        print(A[L-1:R].count(X))
