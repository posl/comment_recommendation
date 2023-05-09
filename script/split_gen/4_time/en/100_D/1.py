def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append([x, y, z])
    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * (-1) ** (i & 1) + x[1] * (-1) ** (i >> 1 & 1) + x[2] * (-1) ** (i >> 2 & 1)))
        beauty = sum([cake[0] for cake in cakes[:M]])
        tastiness = sum([cake[1] for cake in cakes[:M]])
        popularity = sum([cake[2] for cake in cakes[:M]])
        ans = max(ans, abs(beauty) + abs(tastiness) + abs(popularity))
    print(ans)
