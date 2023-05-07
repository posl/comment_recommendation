def main():
    N, M = map(int, input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: -abs(x[i%3]) if i < 3 else abs(x[i%3]))
        ans = max(ans, sum([abs(sum(cake[j][i%3] for j in range(M))) for i in range(3)]))
    print(ans)
