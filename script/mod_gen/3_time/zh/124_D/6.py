def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            if i == 0 or S[i-1] == '1':
                ans += 1
        else:
            if i == 0 or S[i-1] == '0':
                ans += 1
    ans += 2 * K
    print(min(ans, N-1))

if __name__ == '__main__':
    solve()