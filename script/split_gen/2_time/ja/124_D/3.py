def main():
    N, K = map(int, input().split())
    S = input()
    S = S.replace("0", "1 0").replace("1", "0 1").split()
    S = [int(x) for x in S]
    N = len(S)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        left[i + 1] = left[i] + S[i]
        right[N - 1 - i] = right[N - i] + S[N - 1 - i]
    ans = 0
    for i in range(N + 1):
        l = max(0, i - 2 * K)
        r = min(N, i + 2 * K + 1)
        ans = max(ans, left[i] - left[l] + right[i] - right[r])
    print(ans)
