def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        mask = 1 << i
        count = 0
        for a in A:
            if a & mask:
                count += 1
        ans += (count * (N-count) * mask)
        ans %= (10**9+7)
    print(ans)

if __name__ == '__main__':
    solve()