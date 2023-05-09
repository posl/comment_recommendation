def main():
    S = input()
    T = input()
    N = len(T)
    M = len(S)
    ans = N
    for i in range(M - N + 1):
        cnt = 0
        for j in range(N):
            if S[i + j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)
