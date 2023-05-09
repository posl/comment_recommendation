def main():
    N, M = map(int, input().split())
    S = set(range(1, M + 1))
    for _ in range(N):
        _, *A = map(int, input().split())
        S &= set(A)
    print(len(S))

if __name__ == '__main__':
    main()