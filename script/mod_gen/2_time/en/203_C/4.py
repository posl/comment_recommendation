def solve():
    N, K = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for A, B in AB:
        if K >= A:
            K += B
    print(K)

if __name__ == '__main__':
    solve()