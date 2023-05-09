def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(1, N):
        if S[i - 1] == S[i]:
            ans += 1
    ans = min(ans + 2 * K, N - 1)
    print(ans)
