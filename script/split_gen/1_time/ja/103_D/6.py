def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ab.reverse()
    bridge = [1] * n
    for a, b in ab:
        bridge[a-1] = 0
        bridge[b-1] = 0
        if bridge[a-1] == 0 and bridge[b-1] == 0:
            bridge[b-1] = 1
    print(sum(bridge))
