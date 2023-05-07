def solve(N, M, U, V):
    ans = 0
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            for c in range(b + 1, N + 1):
                if (a, b) in zip(U, V) and (b, c) in zip(U, V) and (c, a) in zip(U, V):
                    ans += 1
    return ans

if __name__ == '__main__':
    solve()