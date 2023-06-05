def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    print(min(ans, N - ans) * 2)
