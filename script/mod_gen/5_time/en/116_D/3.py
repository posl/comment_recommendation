def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        sushi.append(tuple(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kinds = set()
    base = 0
    for i in range(K):
        base += sushi[i][1]
        kinds.add(sushi[i][0])
    ans = base + len(kinds)**2
    for i in range(K, N):
        if sushi[i][0] in kinds:
            continue
        base += sushi[i][1] - sushi[K-1][1]
        kinds.add(sushi[i][0])
        ans = max(ans, base + len(kinds)**2)
    print(ans)
main()
