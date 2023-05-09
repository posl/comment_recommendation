def main():
    N, M = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        cakes.sort(reverse=True, key=lambda x: x[0] if i & 1 else -x[0])
        cakes.sort(reverse=True, key=lambda x: x[1] if i & 2 else -x[1])
        cakes.sort(reverse=True, key=lambda x: x[2] if i & 4 else -x[2])
        ans = max(ans, sum(map(abs, [sum(cake) for cake in zip(*cakes[:M])])))
    print(ans)
