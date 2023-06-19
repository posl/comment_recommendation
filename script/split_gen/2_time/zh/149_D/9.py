def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if T[i] == 'r':
            if i < K or T[i - K] != 'r':
                ans += P
        elif T[i] == 's':
            if i < K or T[i - K] != 's':
                ans += R
        elif T[i] == 'p':
            if i < K or T[i - K] != 'p':
                ans += S
    print(ans)
solve()
