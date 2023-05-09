def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] == S[i-1]:
            ans += 1
    print(min(ans + K * 2, N))
