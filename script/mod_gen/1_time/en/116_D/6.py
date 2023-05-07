def main():
    N, K = map(int, input().split())
    Sushi = [tuple(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    types = set()
    ans = 0
    base = 0
    for i in range(K):
        base += Sushi[i][1]
        types.add(Sushi[i][0])
    ans = base + len(types)**2
    for i in range(K, N):
        if len(types) == K:
            break
        if Sushi[i][0] in types:
            continue
        types.add(Sushi[i][0])
        for j in range(K-1, -1, -1):
            if Sushi[j][0] in types:
                continue
            base += Sushi[i][1] - Sushi[j][1]
            types.add(Sushi[j][0])
            break
        ans = max(ans, base + len(types)**2)
    print(ans)

if __name__ == '__main__':
    main()