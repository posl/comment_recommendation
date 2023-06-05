def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for j in range(N - i):
            if S[j] != S[j + i]:
                ans[i - 1] = i
                break
    for i in range(N - 1):
        print(ans[i])
