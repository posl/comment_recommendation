def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    prev = 0
    for a, b in bridges:
        if prev < a:
            ans += 1
            prev = b - 1
    print(ans)
