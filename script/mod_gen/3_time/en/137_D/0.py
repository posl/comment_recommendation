def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    jobs = sorted(zip(A, B))
    ans = 0
    i = 0
    while i < N:
        a, b = jobs[i]
        if a > M:
            break
        ans += b
        M -= a
        i += 1
    print(ans)

if __name__ == '__main__':
    solve()