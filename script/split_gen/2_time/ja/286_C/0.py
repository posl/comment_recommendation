def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        ans = 0
    else:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
    print(ans)
