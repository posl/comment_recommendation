def solve():
    N, M = map(int, input().split())
    requests = [tuple(map(int, input().split())) for _ in range(M)]
    bridge = [0] * (N + 1)
    for a, b in requests:
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(1))

if __name__ == '__main__':
    solve()