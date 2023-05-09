def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

if __name__ == '__main__':
    main()