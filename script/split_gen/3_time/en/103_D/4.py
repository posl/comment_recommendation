def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    while bridges:
        a, b = bridges.pop()
        ans += 1
        while bridges and bridges[-1][0] >= a:
            bridges.pop()
    print(ans)
