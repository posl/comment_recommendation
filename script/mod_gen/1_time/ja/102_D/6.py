def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = [A[0]]
    Q = [A[0]]
    R = [A[0]]
    S = [A[0]]
    for i in range(1, N):
        P.append(P[i - 1] + A[i])
        Q.append(Q[i - 1] + A[N - 1 - i])
        R.append(R[i - 1] + A[i])
        S.append(S[i - 1] + A[N - 1 - i])
    P = P[1:]
    Q = Q[1:]
    R = R[1:]
    S = S[1:]
    Q = Q[::-1]
    S = S[::-1]
    ans = 10**18
    for i in range(3):
        for j in range(i + 1, N - 1):
            ans = min(ans, max(P[i], Q[j], R[j] - R[i], S[N - 1] - S[j]) - min(P[i], Q[j], R[j] - R[i], S[N - 1] - S[j]))
    print(ans)

if __name__ == '__main__':
    main()