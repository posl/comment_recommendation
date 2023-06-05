def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for k in range(40, -1, -1):
        count = 0
        for a in A:
            if a & (1 << k):
                count += 1
        if count <= N // 2:
            if ans + (1 << k) <= K:
                ans += (1 << k)
    f = 0
    for a in A:
        f += ans ^ a
    print(f)

if __name__ == '__main__':
    solve()