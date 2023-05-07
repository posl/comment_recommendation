def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N+1):
        print(sorted(P[:i])[K-1])

if __name__ == '__main__':
    solve()