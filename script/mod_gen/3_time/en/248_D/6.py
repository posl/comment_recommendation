def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for L, R, X in queries:
        print(A[L-1:R].count(X))

if __name__ == '__main__':
    main()