def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    ans = 10**9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(S[i], S[j]-S[i], S[k]-S[j], S[N]-S[k]) - min(S[i], S[j]-S[i], S[k]-S[j], S[N]-S[k]))
    print(ans)
