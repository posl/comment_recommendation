def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    if ans == 0:
        print(1)
        return
    if ans == N:
        print(N)
        return
    for i in range(N):
        if S[i] == '0':
            ans += 1
            break
    for i in range(N - 1, -1, -1):
        if S[i] == '0':
            ans += 1
            break
    ans = min(ans + 2 * K, N)
    print(ans)
