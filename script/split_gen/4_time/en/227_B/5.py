def solve():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if 4 * S[i] * S[j] + 3 * S[i] + 3 * S[j] == 4 * S[i] * S[j] + 3 * S[i] + 3 * S[j]:
                ans += 1
    print(ans)
