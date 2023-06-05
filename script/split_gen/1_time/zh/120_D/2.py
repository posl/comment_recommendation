def main():
    n, m = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(m)]
    bridge.sort(key=lambda x: x[1])
    print(bridge)
    island = [0] * n
    for i, j in bridge:
        island[j - 1] = max(island[i - 1] + 1, island[j - 1])
    print(island)
    ans = sum(island)
    for i, j in reversed(bridge):
        ans -= island[i - 1]
        island[i - 1] = max(island[i - 1], island[j - 1] + 1)
        ans += island[i - 1]
        print(ans)
    print(ans)
