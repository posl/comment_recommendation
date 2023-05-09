def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            if S[i - 1] == S[i]:
                ans += 1
    ans += 2 * K
    ans = min(ans, N - 1)
    print(ans)
