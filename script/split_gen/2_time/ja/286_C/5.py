def main():
    N, A, B, S = read()
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans += min(A, B)
    print(ans)
