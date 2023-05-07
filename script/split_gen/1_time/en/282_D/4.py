def main():
    N, M = map(int, input().split())
    if M == 0:
        print(int(N * (N - 1) / 2))
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[1])
    ans = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if [i, j] not in edges and [j, i] not in edges:
                ans += 1
    print(ans)
main()
