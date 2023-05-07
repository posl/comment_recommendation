def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        A_i, P_i, X_i = map(int, input().split())
        A.append(A_i)
        P.append(P_i)
        X.append(X_i)
    ans = -1
    for i in range(N):
        if X[i] > A[i]:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

if __name__ == '__main__':
    main()