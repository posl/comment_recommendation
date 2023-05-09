def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 10 ** 18
    for i in range(N):
        ans = min(ans, abs(S[i + 1] - S[0] - i * (S[i + 1] - S[0])))
    print(ans)
