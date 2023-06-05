def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for j in range(N - i):
            if S[j] != S[i + j]:
                ans[i - 1] = i
                break
    print(*ans, sep='\n')
