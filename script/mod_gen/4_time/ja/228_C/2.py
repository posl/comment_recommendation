def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    R = []
    for p in P:
        R.append(sum(p))
    R.sort(reverse=True)
    print("Yes" if R[K-1] > R[K] else "No")

if __name__ == '__main__':
    solve()