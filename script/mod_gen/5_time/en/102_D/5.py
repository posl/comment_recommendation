def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(0, N):
        S.append(S[-1] + A[i])
    res = 10**9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            res = min(res, abs(S[i] - S[0] - (S[j] - S[i])) + abs(S[-1] - S[j] - (S[i + 1] - S[j])))
    print(res)

if __name__ == '__main__':
    main()