def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "L":
            ans += 1
        else:
            break
    for i in range(N-1, -1, -1):
        if S[i] == "R":
            ans += 1
        else:
            break
    if ans < N:
        if K >= 1:
            ans += 2 * K - 1
    print(min(ans, N))
