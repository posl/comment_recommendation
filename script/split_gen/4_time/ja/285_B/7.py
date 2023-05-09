def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for l in range(N - i):
            if S[l] != S[l + i]:
                ans[i - 1] = i
                break
    for i in ans:
        print(i)
