def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N // 2):
        if S[i] != S[N - i - 1]:
            ans += min(A, B)
    print(ans)
