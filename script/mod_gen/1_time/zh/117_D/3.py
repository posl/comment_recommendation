def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    bit = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        if cnt <= N - cnt and bit + (1 << i) <= K:
            bit += 1 << i
    ans = 0
    for a in A:
        ans += bit ^ a
    print(ans)

if __name__ == '__main__':
    solve()