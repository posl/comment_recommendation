def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    for i in range(M):
        ans += (i+1) * A[i]
    tmp = ans
    for i in range(N-M):
        tmp = tmp + (M+1) * A[i+M] - S[i+M+1] + S[i+1]
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()