def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for a, b in bridges:
        if bridge < a:
            ans += 1
            bridge = b-1
    print(ans)
