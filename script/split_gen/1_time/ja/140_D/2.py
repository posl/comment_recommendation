def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] != S[i - 1]:
            ans += 1
    if ans % 2 == 0:
        ans -= 1
    print(min(ans + 2 * K, N))
