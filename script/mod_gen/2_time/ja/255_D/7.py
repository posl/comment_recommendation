def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    S = sum(A)
    S1 = S - N * X[0]
    S2 = S - N * X[-1]
    for i in range(1, Q):
        S1 -= X[i] - X[i-1]
        S2 -= X[Q-i-1] - X[Q-i]
        print(S1 + S2)

if __name__ == '__main__':
    main()