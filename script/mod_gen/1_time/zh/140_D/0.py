def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    ans += min(2*K, N-1)
    print(ans)

if __name__ == '__main__':
    solve()