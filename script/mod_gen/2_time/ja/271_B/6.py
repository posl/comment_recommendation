def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i][0])
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

if __name__ == '__main__':
    main()