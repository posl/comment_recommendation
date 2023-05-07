def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [list(map(int, input().split())) for _ in range(Q)]
    for s, t in S:
        print(A[s-1][t-1])

if __name__ == '__main__':
    main()