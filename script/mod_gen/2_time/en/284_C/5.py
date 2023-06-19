def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    ans = 0
    for i in range(M):
        if i == 0:
            ans += 1
            continue
        if edges[i][0] != edges[i - 1][0] and edges[i][1] != edges[i - 1][1]:
            ans += 1
    print(ans + 1)
main()
