def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            j = i
            while j < N and S[j] == "0":
                j += 1
            ans = max(ans, j - i)
    for i in range(N):
        if S[i] == "1":
            j = i
            while j < N and S[j] == "1":
                j += 1
            ans = max(ans, j - i)
    if ans == N:
        ans += K * 2
    else:
        ans += K
    print(min(ans, N))
solve()

if __name__ == '__main__':
    solve()