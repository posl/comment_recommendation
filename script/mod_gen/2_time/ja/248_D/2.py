def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(R - L - A[L - 1:R].count(X) + 1)

if __name__ == '__main__':
    main()