def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for _ in range(Q):
        L, R, X = [int(x) for x in input().split()]
        print(A[L-1:R].count(X))

if __name__ == '__main__':
    main()