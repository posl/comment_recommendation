def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] != S[-1-i]:
            ans += min(A, B)
    print(ans)
