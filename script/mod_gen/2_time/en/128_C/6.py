def solve():
    N, M = map(int, input().split())
    S = [[int(x) for x in input().split()] for _ in range(M)]
    P = [int(x) for x in input().split()]
    ans = 0
    for i in range(2**N):
        if sum([sum([P[j] if i & 1 << (S[j][k] - 1) else 0 for k in range(1, S[j][0] + 1)]) % 2 for j in range(M)]) == 0:
            ans += 1
    print(ans)
solve()
Thank you for your time!

if __name__ == '__main__':
    solve()