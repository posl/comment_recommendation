def main():
    N, M = map(int, input().split())
    cakes = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2**3):
        sign = [1 if i >> j & 1 else -1 for j in range(3)]
        cakes.sort(key=lambda x: sum(sign[j]*x[j] for j in range(3)), reverse=True)
        ans = max(ans, sum(sum(sign[j]*x[j] for j in range(3)) for x in cakes[:M]))
    print(ans)
