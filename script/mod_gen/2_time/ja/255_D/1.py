def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    S = sum(A)
    for x in X:
        print(S - N * x)

if __name__ == '__main__':
    main()