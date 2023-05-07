def main():
    N, A, B = map(int, input().split())
    S = input()
    if A <= B:
        print(A * (N - 1))
        return
    ans = 0
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans += B
        else:
            ans += A
    print(ans)
