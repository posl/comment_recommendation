def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    cakes.sort(reverse=True, key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]))
    ans = 0
    for i in range(M):
        ans += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    print(ans)
