def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    Q = [sorted(P[i], reverse=True) for i in range(N)]
    R = [sum(Q[i][:3]) for i in range(N)]
    S = sorted(R, reverse=True)
    T = [S.index(R[i]) + 1 for i in range(N)]
    for i in range(N):
        if T[i] <= K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()