def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    for k in K:
        l, r = 0, 10**18
        while r - l > 1:
            m = (l + r) // 2
            cnt = 0
            for a in A:
                cnt += (m + a - 1) // a
            if cnt >= k:
                r = m
            else:
                l = m
        ans.append(r)
    print('
'.join(map(str, ans)))
solve()

if __name__ == '__main__':
    solve()