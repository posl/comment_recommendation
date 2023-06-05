def solve():
    N, Q = map(int, input().split())
    S = input()
    cnt = [0] * N
    for i in range(1, N):
        cnt[i] = cnt[i-1]
        if S[i-1:i+1] == 'AC':
            cnt[i] += 1
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cnt[r-1] - cnt[l-1])
solve()
