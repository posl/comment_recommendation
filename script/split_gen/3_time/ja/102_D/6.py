def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    #print(S)
    ans = 10 ** 9
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            for k in range(j + 1, N - 1):
                a = S[i]
                b = S[j] - S[i]
                c = S[k] - S[j]
                d = S[N] - S[k]
                #print(a, b, c, d)
                ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
    print(ans)
